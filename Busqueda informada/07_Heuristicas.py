#funcion Heuristica

def heuristica(grafo,nodo_inicial,nodo_llegada):

    x1,y1 = grafo[nodo_inicial]['posicion']#posicion del nodo inicial
    x2,y2 = grafo[nodo_llegada]['posicion']#posicion del nodo llegada

    return((x2-x1) **2 +(y2-y1) ** 2)**0.5 #distancia euclidiana
