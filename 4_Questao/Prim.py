class PrimClass:

    Vertices = 0
    Grafo = []
    Inicio = 0

    def __init__(self, grafo, vertices, inicio):
        self.Vertices = vertices
        self.Grafo = grafo
        self.Inicio = inicio
        self.prim()

    def prim(self):
        v = []

        while(len(v) != self.Vertices):
            v.append(0)

        v[self.Inicio] = 1
        pilha = []

        for i in range(0, self.Vertices-1):
            minimo = 999999
            vertice = 0
            e = []

            for j in range(0, self.Vertices):
                if v[j] == 1:
                    for k in range(0, self.Vertices):
                        if v[k] == 0 and self.Grafo[j][k] < minimo:
                            vertice = k
                            e = [j, k]
                            minimo = self.Grafo[j][k]

            v[vertice] = 1
            pilha.append(e)
        print(pilha)
