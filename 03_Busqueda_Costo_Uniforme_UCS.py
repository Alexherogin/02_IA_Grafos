#Practica de costo uniforme para inteligencia artificial

import heapq # para usar la cola de prioridad

#Funcion para encontrar el camino mas corto

def CostoU(greafo,Nodo_Star):
    visitados = set()
    #Cola de prioridad
    cola = [(0,Nodo_Star,())]
    
    while cola:
        (costo_acumulado,Nodo_actual,camino) = heapq.heappop(cola)
        if Nodo_actual in visitados:
            continue

        visitados.add(Nodo_actual)
        print(Nodo_actual)

        for (costo,Nodo_siguiente,direccion) in grafo[Nodo_actual]:
            if Nodo_siguiente not in visitados:
                Nuevo_costo = costo_acumulado + costo
                heapq.heappush(cola,(Nuevo_costo,Nodo_siguiente,camino + (direccion,)))
    return camino 

grafo ={
    'entrada':[('sala',1),('cuarto_PB',1.5)],
    'sala':[('comedor',2),('escaleras',1.8)],
    'comedor':[('sala',2),('cocina',1.5)],
    'cocina':[('comedor',1.5),('cuarto_PB',1.5)],
    'cuarto_PB':[('cocina',1.5),('entrada',1.5),('escaleras',1.5)]

    
    }
CostoU(grafo,'entrada')
