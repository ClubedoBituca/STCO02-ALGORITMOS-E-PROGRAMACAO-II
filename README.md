Algoritmos e Programação 2 (Prof. Pedro Hokama)

Este repositório contém os projetos e implementações desenvolvidas para a disciplina de Algoritmos e Programação 2 (A&P 2). O foco principal da disciplina foi aprofundar o conhecimento em estruturas de dados avançadas, algoritmos de ordenação, técnicas de busca e manipulação de arquivos.

🚀 Conceitos Abordados

Os trabalhos aqui presentes demonstram a aplicação prática dos seguintes conceitos:

1. Tabelas Hash (Hashing) com Resolução de Colisão

    Trabalho Referente: t01.py - Sistema de Receitas e Ingredientes.

    Conceitos Implementados:

        Tabela Hash: Estrutura utilizada para mapear chaves (nomes de receitas ou ingredientes) para índices de acesso rápido.

        Função Hash Personalizada: Implementação de uma função calcular_hash que combina a função ord() e pesos crescentes (mult) para calcular o índice a partir de uma chave (string).

        Resolução de Colisão por Encadeamento (Separate Chaining): Em vez de usar listas ligadas, a colisão é resolvida usando Árvores Binárias de Busca (ABB) em cada slot da tabela. Isso garante busca, inserção e remoção eficientes mesmo em caso de colisões, mantendo as chaves ordenadas dentro do slot.

2. Algoritmos de Ordenação

    Trabalho Referente: t02.py - Sistema de Ranqueamento de Criaturas.

    Conceito Implementado:

        Merge Sort: Algoritmo de ordenação eficiente (O(nlogn)) implementado para ranquear as criaturas.

        Função de Comparação Personalizada: O algoritmo de ordenação utiliza uma função de comparação (compare_creatures) que implementa uma lógica de desempate:

            Ordena primeiramente pelo score (pontuação total) em ordem decrescente.

            Em caso de empate no score, desempata pelo nome da criatura em ordem crescente (lexicográfica).

    Conceitos Adicionais:

        Uso do módulo csv para manipulação de arquivos.

        Cálculo de pontuação (ranking ponderado) baseado em vetores de pesos fornecidos pelo usuário.

3. Árvores de Busca Balanceadas

    Trabalho Referente: t03rubro.py e t03avl.py - Jogo do Número Mais Próximo.

    Conceitos Implementados:

        Árvore Rubro-Negra (Red-Black Tree): Implementação de uma Árvore Binária de Busca Auto-Balanceada (t03rubro.py).

            Operações Essenciais: Rotação à Esquerda (rotacionaEsquerda), Rotação à Direita (rotacionaDireita) e Subida da Cor Vermelha (sobeVermelho).

            Regras de Inserção: Lógica de balanceamento aplicada durante a inserção (insere_aux) para garantir que a árvore permaneça balanceada (propriedades Rubro-Negras).

        Árvore AVL: Implementação de outra Árvore Binária de Busca Auto-Balanceada (t03avl.py).

            Métrica de Balanceamento: Fator de Balanceamento (fb) e uso da altura de cada nó.

            Rotações: Rotação Simples à Esquerda (rotacaoEsquerda) e à Direita (rotacaoDireita), e Rotacões Duplas (aplicação de duas rotações simples, como a LR e RL).

        Busca Especializada: Função encontra_mais_proximo que busca o elemento da árvore com a menor diferença absoluta em relação a um valor x dado.

4. Árvores B (Estruturas de Dados em Disco)

    Trabalho Referente: t04.py - Busca em Árvore B.

    Conceitos Implementados:

        Estrutura de Nó em Disco: Simulação de um nó de Árvore B onde as informações de chaves e referências de filhos são carregadas sob demanda de um arquivo externo (simulando acesso a disco) através da função carrega_arquivo.

        Busca (Search): Implementação do algoritmo de busca (busca) que navega pela estrutura, chamando a função de carregamento (carrega_arquivo) recursivamente apenas quando necessário para acessar um nó filho.

        M-Vias: O nó armazena múltiplas chaves (chaves) e ponteiros para os filhos (filhos), caracterizando a estrutura de árvore M-vias.
