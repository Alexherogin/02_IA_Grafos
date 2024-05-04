#busqueda por A* y AO*
import heapq

def A_star(grafo,inicio,meta): #
    open_set=[]
    heapq.heappush(open_set,(0,inicio)) # se genera una cola de prioriodad empezando desde el nodo inicial

    camino= {} #diccionario para registro de nodos 
    g= {nodo:float('inf')for nodo in grafo} # se crao una variable y diccionaro para almacenar el costo real (g(n))
    g[inicio]=0 # inicio del costo en 0
    f={nodo:float('inf')for nodo in grafo}# diccionario ara almacenar funcion (f(n)) para el inicio del nodo
    f= heuristica (inicio,meta)

    while open_set:
       _, nodo_actual=heapq.heappop(open_set)# se busca el nodo con valor menor de (f(n))
       if nodo_actual==meta:
           return reconstruir_camino(camino,meta)# 
       
       for nodo_vecino in grafo[nodo_actual]: # busca los nodos vecino del nodo actual en busqueda
           nuevo_g=g[nodo_actual]+grafo[nodo_actual][nodo_vecino]#  calcula nuevo costo por cambio de nodo
           if nuevo_g<g[nodo_vecino]:#comparacion si el nuevo costo es menor al nodo que paso 
              #actualisa el dicionario al de menor costo
               camino[nodo_vecino]=nodo_actual
               g[nodo_vecino]=nuevo_g
               f[nodo_vecino]=nuevo_g+heuristica(nodo_vecino,meta)
               heapq.heappush(open_set,(f[nodo_vecino],nodo_vecino))
    return None

def heuristica(nodo,meta):# funcion heuristica 
    x1,y1=nodo
    x2,y2=meta

    return abs(x1-x2)+abs(y1-y2)

def reconstruir_camino(camino,nodo_actual):
    paso=[nodo_actual]
    while nodo_actual in camino:
        nodo_actual=camino[nodo_actual]
        paso.append(nodo_actual)
    paso.reverse() #
    return paso

def AO_star(grafo,inicio,meta):
    open_set=[]
    heapq.heappush(open_set,(0,inicio))  #
    camino={}
    g={nodo:float('inf')for nodo in grafo}
    g=[inicio]=0

    while open_set: 
        _,nodo_actual= heapq.heappop(open_set)
        if nodo_actual == meta:
            return reconstruir_camino(camino,meta)
        for vecino in grafo[nodo_actual]:
            nuevo_g= g [nodo_actual] + grafo[nodo_actual][vecino]
            if nuevo_g<g[vecino]:
                camino[vecino] = nodo_actual
                g[vecino]=nuevo_g
                f=g[vecino]+heuristica(vecino,meta)
                heapq.heappush(open_set,(f,vecino))
                open_set.append((f,vecino))
                open_set.sort(key=lambda x:[0])
    return None




            

            