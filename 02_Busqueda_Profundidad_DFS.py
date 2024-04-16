#Empezando tema DFS Busqueda por profundidad IA

def dfs_profundidad(grafo, Inicio, recorridos=None, nodos=None):#funcion para  inicio del grafo
    if recorridos is None:
        recorridos = set()
    recorridos.add(Inicio)#Agregamos el nodo a la lista de recorridos

    for x in range (len(grafo[Inicio])):
        if grafo[Inicio][x] == 1 and nodos[x] not in recorridos:
            dfs_profundidad(grafo, x, recorridos, nodos)
    print(recorridos)
nodos= {
   'a':1 ,
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
}

grafo_matriz= [
     #a b c d e f g
    [-1,1,1,0,0,0,0],#a
    [ 0,0,0,1,1,0,0],#b
    [ 0,0,0,0,0,1,1],#c
    [ 0,0,0,0,0,0,0],#d
    [ 0,0,0,0,0,0,0],#e
    [ 0,0,0,0,0,0,0],#f
    [ 0,0,0,0,0,0,0],#g
]
print('recoridos de profundidad:\n')
print (dfs_profundidad(grafo_matriz, 0,nodos=nodos))