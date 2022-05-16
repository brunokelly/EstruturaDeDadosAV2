class ClasseDFS:

    Vertices = 0

    def __init__(self, numVertices):
        self.Vertices = numVertices

    def Adicionar(self, grafo, inicio, visitados, arvore, pai, nivel, destino):
        for i in range(self.Vertices):
            if grafo[inicio][i] == 1 and not visitados[i]:
                visitados[i] = True
                arvore.append((i, inicio, nivel+1))
                pai[i] = inicio
                self.Adicionar(grafo, i, visitados, arvore,
                               pai, nivel+1, destino)

    def DFS(self, grafo, destino: int, inicio: int):
        visitados = [False] * self.Vertices
        visitados[inicio] = True
        pilha = []
        pilha.append((inicio, 0))
        arvore = [(inicio, None, 0)]
        pai = [None] * self.Vertices
        self.Adicionar(grafo, inicio, visitados, arvore, pai, 0, destino)

        n = 0
        caminho = []
        arvoreReversa = [arvore[::-1]]

        for vert in [arvoreReversa[0]][0]:

            if(n == len(arvore) - 1):
                break

            if [arvoreReversa[0]][0][n+1][0] == vert[1]:
                if len(caminho) == 0:
                    caminho.append([arvoreReversa[0]][0][n+1])
                elif len(caminho) != 0 and caminho[-1][1] == [arvoreReversa[0]][0][n+1][0]:
                    caminho.append([arvoreReversa[0]][0][n+1])

            n = n + 1
        
        print("\nMelhor Caminho: ")
        caminho = caminho[::-1]

        for vert in caminho:
            print(vert[0])
        print(destino)
