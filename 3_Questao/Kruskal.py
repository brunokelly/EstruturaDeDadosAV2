V = 6
G = [[0,	337,	1846,	1464,	0,	0,	2704],
     [337,	0,	0,	1235,	2342,	0,	0],
     [1846,	0,	0,	802,	0,	740,	867],
     [1464,	1235,	802,	0,	1121,	0,	0],
     [0,	2342,	0,	1121,	0,	1090,	1258],
     [0,	0,	740,	0,	1090,	0,	187],
     [2704,	0,	867,	0,	1258,	187,	0]]

A = []

for i in range(V):
    for j in range(i+1,V):
        if(G[i][j]!=0):
            A.append((i,j,G[i][j]))

A.sort(key=lambda x: x[2])

AU = []

def checkVizinhos(visitados,grafo,atual):
    if visitados[atual]:
        return True
    visitados[atual]=True
    for i in grafo:
        if i[0]==atual and checkVizinhos(visitados,grafo,i[1]):
            return True
    return False
    

def isCiclico(grafo):
    verificados = [False] * V
    for i in grafo:
        if verificados[i[0]]:
            continue 
        else:
            verificados[i[0]]=True
        visitados = [False] * V
        if checkVizinhos(visitados,grafo,i[0]):
            return True;
    return False;

for i in A:    
   if not isCiclico(AU+[i]):
       AU.append(i)
   

for i in AU:
    print(i)



        