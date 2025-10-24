import os

class noh:
    def __init__(self, fileName_="None"):
        self.fileName = fileName_
        self.carregado = False
        self.folha = True
        self.chaves = []
        self.filhos = []

    def carrega_arquivo(self, nome_arquivo):
        print("📂 Lendo:", nome_arquivo)
        self.carregado = True

        with open(nome_arquivo, "r") as f:
            linhas = [linha.strip() for linha in f.readlines() if linha.strip()]

        self.chaves = []
        self.filhos = []

        # formato alternado: filho, chave, filho, chave, filho...
        for i, linha in enumerate(linhas):
            if i % 2 == 0:
                # linha de filho
                if linha != "None":
                    caminho_filho = os.path.join(os.path.dirname(nome_arquivo), linha)
                    self.filhos.append(noh(caminho_filho))
                else:
                    self.filhos.append(None)
            else:
                # linha de chave
                try:
                    self.chaves.append(int(linha))
                except ValueError:
                    print(f"⚠️ Linha de chave inválida em {nome_arquivo}: '{linha}'")

        # Ajuste final: pode faltar um último filho
        if len(self.filhos) == len(self.chaves):
            self.filhos.append(None)

        # define se é folha
        self.folha = all(filho is None for filho in self.filhos)



class arvoreB:
    def __init__(self, t, filename):
        self.t = t
        self.raiz = noh(filename)

    def busca(self, k, x):
        if not x.carregado:
            x.carrega_arquivo(x.fileName)
        i = 0
        while i < len(x.chaves) and k > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and k == x.chaves[i]:
            return (x, i)
        elif x.folha:
            return None
        else:
            return self.busca(k, x.filhos[i])


# ==========================
# EXECUÇÃO AUTOMÁTICA
# ==========================

pasta = os.path.join(os.path.dirname(__file__), "arquivos")

print("\n🌳 TESTE AUTOMÁTICO DAS ÁRVORES NA PASTA 'arquivos/'")
print("=" * 55)

# percorre todos os arquivos .tree da pasta
arquivos_tree = sorted([f for f in os.listdir(pasta) if f.endswith(".tree")])

# faz a busca automática para as chaves contidas em cada nó
for nome_arquivo in arquivos_tree:
    caminho = os.path.join(pasta, nome_arquivo)
    print(f"\n--- Analisando {nome_arquivo} ---")

    arv = arvoreB(2, caminho)
    arv.raiz.carrega_arquivo(caminho)

    # busca todas as chaves que estão nesse arquivo e um valor inexistente
    for chave in arv.raiz.chaves + [999999]:
        resultado = arv.busca(chave, arv.raiz)
        if resultado is None:
            print(f"❌ {chave} não encontrado")
        else:
            print(f"✅ {chave} encontrado em {nome_arquivo}")

print("\n✅ Teste completo finalizado.")
