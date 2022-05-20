class Dijkstra:

    def DistanciaMinima(self,distancias,pilha):
        valorMinimo = float("Inf")
        indexValorMinimo = -1

        for i in range(len(distancias)):

            if distancias[i] < valorMinimo and i in pilha:
                valorMinimo = distancias[i]
                indexValorMinimo = i

        return indexValorMinimo
 
    def caminhoPai(self, caminhoPai, atual):
        if caminhoPai[atual] == -1 :
            print(atual + 1, end=" ")
            return
        self.caminhoPai(caminhoPai , caminhoPai[atual])
        print (atual + 1, end=" ")

    def dijkstra(self, grafo, inicio, destinos):
 
        linha = len(grafo)
        coluna = len(grafo[0])
        distancias = [float("Inf")] * linha
        caminhoPai = [-1] * linha
        distancias[inicio] = 0
        pilha = []

        for i in range(linha):
            pilha.append(i)

        while pilha:
            valorMinimo = self.DistanciaMinima(distancias,pilha)  
            pilha.remove(valorMinimo)
            for i in range(coluna):
                if grafo[valorMinimo][i] and i in pilha:
                    if distancias[valorMinimo] + grafo[valorMinimo][i] < distancias[i]:
                        distancias[i] = distancias[valorMinimo] + grafo[valorMinimo][i]
                        caminhoPai[i] = valorMinimo
 
        for i in range(1, len(distancias)):
           if i in destinos: 
                print("\nDestino: %d para %d | Distancia: %.2f | " % (inicio + 1, i , float(distancias[i])), end=" ")
                self.caminhoPai(caminhoPai ,i)