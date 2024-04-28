#Practica de costo uniforme para inteligencia artificial

import heapq # para usar la cola de prioridad

#Funcion para encontrar el camino mas corto

def CostoU(grafo,Nodo_Star): #Nodo_Star es el nodo inicial  
    visitados = set()
    #Cola de prioridad
    cola = [(0,Nodo_Star,)]
    
    while cola: 
        (costo_acumulado,Nodo_actual) = heapq.heappop(cola)
        if Nodo_actual in visitados:
            continue

        visitados.add(Nodo_actual)#Agregamos el nodo a la lista de visitados
        print(f'Paso de nodo:',{Nodo_actual},'Costo acumulado:',{costo_acumulado})

        for Nodo_siguiente,costoT in grafo.get(Nodo_actual,[]):#Obtenemos los nodos adyacentes
            if Nodo_siguiente not in visitados:#Si el nodo no esta en la lista de visitados
                Nuevo_costo = costo_acumulado + int(costoT)
                heapq.heappush(cola,(Nuevo_costo,Nodo_siguiente, ))#Agregamos el nodo a la cola de prioridad
    return visitados

grafo = { 'entrada':[('sala',1),('cuarto_PB',1)],#Agregamos los nodos y sus adyacencias
    'sala':[('comedor',2),('escaleras',2)],
    'cuarto_PB':[],
    'comedor':[('baño_PB',2),('cocina',4)],
    'baño_PB':[],
    'cocina':[('cuarto_lavado',5),('patio_Tracero',5)],
    'cuarto_lavado':[],
    'Patio_Tracero':[],
    'escaleras':[('planta_Alta',2)],
    'planta_Alta':[('Cuarto_PA_1',9),('vestibulo',8),('baño_PA',9),('cuarto_2_PA',11)],
    'Cuarto_PA_1':[],
    'vestibulo':[],
    'baño_PA':[],
    'cuarto_2_PA':[('baño_cuarto',11.),('valcon',12)],
    'baño_cuarto':[],
    'valcon':[],}
CostoU(grafo,'entrada')
