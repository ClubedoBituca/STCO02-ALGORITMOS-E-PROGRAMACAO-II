#Não mexa aqui.
import random
import time
MINIMO = 1
MAXIMO = 9_223_372_036_854_775_807
random.seed(42)  # Para garantir a reprodutibilidade dos testes

#SEU TRABALHO COMEÇA DAQUI PRA FRENTE
#VOCÊ PODE MODIFICAR A CLASSE NOH E CRIAR
#FUNÇÕES ADICIONAIS 

#Quando você estiver submetendo no RunCodes, mude para True
ESTOU_SUBMETENDO_NO_RUNCODES = True

def insere(raiz, dado):
    raiz = insere_avl(raiz, dado)
    raiz.cor = False
    return raiz

def em_ordem(no):
    if no is not None:
        em_ordem(no.esq)
        print(no.dado, end=" ")
        em_ordem(no.dir)

def encontra_mais_proximo(no, x):
    mais_proximo = no.dado
    while no:
        if abs(no.dado - x) < abs(mais_proximo - x) or \
           (abs(no.dado - x) == abs(mais_proximo - x) and no.dado < mais_proximo):
            mais_proximo = no.dado
        if x < no.dado:
            no = no.esq
        elif x > no.dado:
            no = no.dir
        else:
            return no.dado
    return mais_proximo


class node:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura = 0

def altura(y):
    if y is None:
        return -1
    return y.altura

def rotacaoDireita(y):
    x = y.esq
    y.esq = x.dir
    x.dir = y
    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    x.altura = max(altura(x.esq), altura(x.dir)) + 1
    return x

def rotacaoEsquerda(y):
    x = y.dir
    y.dir = x.esq
    x.esq = y
    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    x.altura = max(altura(x.esq), altura(x.dir)) + 1
    return x

def fb(y):
    return altura(y.esq) - altura(y.dir)

def insere_avl(y, dado):
    if y is None:
        return node(dado)
    if dado < y.dado:
        y.esq = insere_avl(y.esq, dado)
        if fb(y) == 2:
            if dado > y.esq.dado:
                y.esq = rotacaoEsquerda(y.esq)
            y = rotacaoDireita(y)
    elif dado > y.dado:
        y.dir = insere_avl(y.dir, dado)
        if fb(y) == -2:
            if dado < y.dir.dado:
                y.dir = rotacaoDireita(y.dir)
            y = rotacaoEsquerda(y)
    else:
        return y
    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    return y
  
##Não mexa aqui.
def inicializa_arvore(n):
  numeros = random.sample(range(MINIMO, MAXIMO), n)
  #Essa linha de baixo é só para deixar o problema
  #mais difícil. Deixe assim.
  numeros.sort()
  raiz = None
  for num in numeros:
    raiz = insere(raiz, num)
  return raiz

def insere_novos_numeros(arvore, n):
  numeros = random.sample(range(MINIMO, MAXIMO), n)
  for num in numeros:
    arvore = insere(arvore, num)
  return arvore


nivel = int(input("Digite o nivel do jogo 1-fácil, 2-normal, 3-difícil, 4-insano: "))
if nivel == 1:
  MAXIMO = 100
  n = 5
elif nivel == 2:
  MAXIMO = 1000
  n = 100
elif nivel == 3:
  n = 5
else:
  n = 50000

arvore = inicializa_arvore(n)
print("\nNúmeros inseridos no jogo:")
if not ESTOU_SUBMETENDO_NO_RUNCODES:
  em_ordem(arvore)
x = random.randint(MINIMO, MAXIMO)
print(f"\n\nQual o valor mais próximo de {x} digite -1 para sair:")

inicio = time.time()
chute = int(input(""))
print()
while chute >= 0:
  #Não é eficiente ficar encontrando o mais próximo
  #toda vez, mas está assim para deixar o problema mais difícil.
  #Deixe assim.
  mais_proximo = encontra_mais_proximo(arvore, x)
  if chute == mais_proximo:
    fim = time.time()
    tempo = fim - inicio
    print(f"Parabéns! Você acertou! O número mais próximo de {x} é {mais_proximo}.")
    if not ESTOU_SUBMETENDO_NO_RUNCODES:
      print(f"Você levou {tempo:.2f} segundos.")
    arvore = insere_novos_numeros(arvore, 3)
    
    if not ESTOU_SUBMETENDO_NO_RUNCODES:
      print("\n**************************")
      print("Números inseridos no jogo:")
      em_ordem(arvore)
    x = random.randint(MINIMO, MAXIMO)
    print(f"\n\nQual o valor mais próximo de {x}:")
    inicio = time.time()
    chute = int(input(""))
  else:
    chute = int(input(f"\nErrou! {chute} não é a resposta!\nTente novamente: "))

print("Saindo!")  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
