# Empezando con los primeros pasos para el desarrollo de un proyecto para comprender la Inteligencia artificial

from collections import deque

def Anchura(grafo, nodo_Star): # Funcion para el recorrido en anchura
    visitado = set ()
    cola = deque ([nodo_Star])

   # cola.append(nodo_Star)# Agregamos el nodo inicial a la cola
    while cola:
        nodo = cola.popleft()
        print(nodo)
        if nodo not in visitado:# Si el nodo no esta en la lista de visitados
            visitado.add(nodo)

            for vecino, _ in grafo.get(nodo,[]):
                cola.append(vecino)# Agregamos los vecinos a la cola

    return visitado# Retornamos los nodos visitados

grafo ={'entrada':[('sala' ,1 ),('cuarto_PB',1)],# Creamos el grafo
        'sala':[('comedor',1),('escaleras',1)],
        'cuarto_PB':[],
        'comedor':[('baño_PB',1), ('cocina',1)],
        'baño_PB':[],
        'cocina':[('cuarto_lavado',1),('patio tracero',1)],
        'cuarto_lavado':[],
        'patio_tracero':[],
        'escaleras':[('planta_alta',1)],
        'planta_alta':[('cuarto_1_PA',1),('vestibulo',1),('baño_PA',1),('cuarto_2_PA',1)],
        'cuarto_1_PA':[],
        'vestibulo':[],
        'baño_PA':[],
        'cuarto_2_PA':[('baño_cuarto',1)],
        'baño':[]}# finalizar el grafo

Anchura(grafo,'entrada')