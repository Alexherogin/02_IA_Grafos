#busqueda por A* y AO*
import heapq

def A_star(grafo,inicio,meta): #
    open_set=[]
    heapq.heappush(open_set,(0,inicio)) 

    camino= {}
    g= {nodo:float('inf')for nodo in grafo}
    g[inicio]=0
    f={nodo:float('inf')for nodo in grafo}
    f= heuristica (inicio,meta)
    while open_set:
       _, nodo_actual=heapq.heappop(open_set)
       if nodo_actual==meta:
           return reconstruir_camino(camino,meta)
       
       for nodo_vecino in grafo[nodo_actual]:
           nuevo_g=g[nodo_actual]+grafo[nodo_actual][nodo_vecino]
           if nuevo_g<g[nodo_vecino]:
               camino[nodo_vecino]=nodo_actual
               g[nodo_vecino]=nuevo_g
               f[nodo_vecino]=nuevo_g+heuristica(nodo_vecino,meta)
               heapq.heappush(open_set,(f[nodo_vecino],nodo_vecino))
    return None

def heuristica(nodo,meta):
    x1,y1=nodo
    x2,y2=meta

    return abs(x1-x2)+abs(y1-y2)

def reconstruir_camino(camino,nodo_actual):
    paso=[nodo_actual]
    while nodo_actual in camino:
        nodo_actual=camino[nodo_actual]
        paso.append(nodo_actual)
    paso.reverse()
    return paso

def AO_star(grafo,inicio,meta):
    open_set=[]
    heapq.heappush(open_set,(0,inicio))
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




            

            