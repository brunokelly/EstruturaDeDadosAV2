class Dijkstra:
    Vertices = 0
    Grafo = []
    Inicio = 0
    Destino = 0

    def __init__(self, grafo, vertices, inicio, destino):
        self.Vertices = vertices
        self.Grafo = grafo
        self.Inicio = inicio
        self.Destino = destino
        self.prim()

    def prim(self):
        visitados = [False] * self.Vertices
        visitados[self.Inicio] = True
        pilha = []

        for i in range(1, self.Vertices-1):
            minimo = 999999
            vertice = 0
            e = []

            for j in range(1, self.Vertices):
                if visitados[j] == True:
                    for k in range(0, self.Vertices):
                        if visitados[k] == False and self.Grafo[j][k] < minimo:
                            vertice = k
                            e = [j, k]
                            minimo = self.Grafo[j][k]

            visitados[vertice] = True
            pilha.append(e)
            
        print(pilha)


