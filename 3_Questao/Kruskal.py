class Kruskal: 
    AU = []
    Vertice = 0
    Grafo = []
    Auxiliar = []
    Visitados = []
    Verificados = []
    A = []
    Lugares = {}
    
    def __init__(self, vertices, grafos, lugar):
        self.Vertice = vertices
        self.Grafo = grafos
        self.Lugares = lugar

        for i in range(self.Vertice):
            for j in range(i+1,self.Vertice):
                if(self.Grafo[i][j]!=0):
                    self.A.append((i,j,self.Grafo[i][j]))

        self.A.sort(key=lambda x: x[2])

        for i in self.A:    
           if not self.isCiclico(self.AU+[i]):
               self.AU.append(i)

        for i in self.AU:
            lugarUm = self.Lugares[i[0]]
            lugarDois = self.Lugares[i[1]]
            print(lugarUm + ' - ' + lugarDois + '| Custo: ' + str(i[2]))


        
    def checkVizinhos(self,grafo, atual):

        if self.Visitados[atual]:
            return True

        self.Visitados[atual]=True

        for i in grafo:

            if i[0]==atual and self.checkVizinhos(grafo,i[1]):
                return True

        return False
    

    def isCiclico(self, grafoT):
        self.Verificados = [False] * self.Vertice

        for i in grafoT:

            if self.Verificados[i[0]]:
                continue 
            else:
                self.Verificados[i[0]]=True

            self.Visitados = [False] * self.Vertice

            if self.checkVizinhos(grafoT, i[0]):
                return True;

        return False;

    



        