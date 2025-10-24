
class NoArvore:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None

class TabelaHash:
    def __init__(self, tamanho=29):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def calcular_hash(self, chave):
        mult = 1
        hash_value = 0
        for c in chave:
            hash_value += mult * ord(c)
            mult += 1
        return hash_value % self.tamanho
    
    def inserir(self, chave, valor):
        indice = self.calcular_hash(chave)
        if self.tabela[indice] is None:
            self.tabela[indice] = NoArvore(chave, valor)
        else:
            self._inserir_arvore(self.tabela[indice], chave, valor)
    
    def _inserir_arvore(self, no, chave, valor):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = NoArvore(chave, valor)
            else:
                self._inserir_arvore(no.esquerda, chave, valor)
        elif chave > no.chave:
            if no.direita is None:
                no.direita = NoArvore(chave, valor)
            else:
                self._inserir_arvore(no.direita, chave, valor)
    
    def buscar(self, chave):
        indice = self.calcular_hash(chave)
        if self.tabela[indice] is None:
            return None
        return self._buscar_arvore(self.tabela[indice], chave)
    
    def _buscar_arvore(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.valor
        elif chave < no.chave:
            return self._buscar_arvore(no.esquerda, chave)
        else:
            return self._buscar_arvore(no.direita, chave)
    
    def imprimir_tabela(self):
        for i in range(self.tamanho):
            if self.tabela[i] is None:
                print("None", end="")
            else:
                self._imprimir_arvore_formatado(self.tabela[i])
            print()
    
    def _imprimir_arvore_formatado(self, no):
        if no is None:
            print("None", end="")
            return
        
        print(f"({no.chave}, ", end="")
        self._imprimir_arvore_formatado(no.esquerda)
        print(", ", end="")
        self._imprimir_arvore_formatado(no.direita)
        print(")", end="")

def ler_arquivo(nome_arquivo):
    tabela_receitas = TabelaHash()
    tabela_itens = TabelaHash()
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        receita_atual = None
        ingredientes = []
        
        for linha in arquivo:
            linha = linha.strip()
            if not linha:  
                if receita_atual is not None and ingredientes:
                    tabela_receitas.inserir(receita_atual, ingredientes)
                    
                    for ingrediente, _ in ingredientes:
                        receitas_do_item = tabela_itens.buscar(ingrediente)
                        
                        if receitas_do_item is None:
                            tabela_itens.inserir(ingrediente, [receita_atual])
                        else:
                            receitas_do_item.append(receita_atual)
                
                receita_atual = None
                ingredientes = []
                continue
            
            if receita_atual is None:  
                receita_atual = linha
            else:  
                partes = linha.split()
                if len(partes) >= 2:
                    quantidade = partes[-1]
                    ingrediente = ' '.join(partes[:-1])
                    ingredientes.append((ingrediente, quantidade))
        
        if receita_atual is not None and ingredientes:
            tabela_receitas.inserir(receita_atual, ingredientes)
            for ingrediente, _ in ingredientes:
                receitas_do_item = tabela_itens.buscar(ingrediente)
                if receitas_do_item is None:
                    tabela_itens.inserir(ingrediente, [receita_atual])
                else:
                    receitas_do_item.append(receita_atual)
    
    return tabela_receitas, tabela_itens

def main():
    try:
        tabela_receitas, tabela_itens = ler_arquivo('craft.txt')
    except FileNotFoundError:
        print("Erro: arquivo 'craft.txt' não encontrado")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    while True:
        entrada = input().strip()
        
        if entrada.lower() == 'q':
            break
        
        if entrada.startswith('r '):
            nome_receita = entrada[2:]
            ingredientes = tabela_receitas.buscar(nome_receita)
            
            if ingredientes is not None:
                print(f"{nome_receita}")
                for ingrediente, quantidade in ingredientes:
                    print(f"{ingrediente} {quantidade}")
            else:
                print(f"{nome_receita}\nNão encontrado")
        
        elif entrada.startswith('i '):
            nome_item = entrada[2:]
            receitas = tabela_itens.buscar(nome_item)
            
            if receitas is not None:
                print(f"{nome_item}")
                for receita in receitas:
                    print(receita)
            else:
                print(f"{nome_item}\nNão encontrado")
        
        elif entrada == 'p r':
            tabela_receitas.imprimir_tabela()
        
        elif entrada == 'p i':
            tabela_itens.imprimir_tabela()
        
        else:
            print("Comando inválido.")

if __name__ == "__main__":
    main()