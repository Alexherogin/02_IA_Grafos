#codigo de voraz primero el mejor
import math
import heapq

def heuristatica (grafo, nodo_inicial, nodo_final):
    
    x1,y1 = grafo[nodo_inicial]['pocicion']
    x2,y2 = grafo[nodo_final]['pocicion']

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#cola de prioridad

def voraz(grafo, nodo_inicio, nodo_final):
    visitados = set()
    cola = [(0, nodo_inicio)]

    while cola:
        _,nodo_inicial= heapq.heappop(cola)

        if nodo_inicial in visitados:
            continue

        visitados.add(nodo_inicial)
        print(f'paso de ruta',nodo_inicial)

        if nodo_inicial == nodo_final:
            break
            
        for nodo_vesino,peso in grafo[nodo_inicial]['ruta']:
            if nodo_vesino not in visitados:
                distancia = peso + heuristatica(grafo, nodo_vesino, nodo_final)
                heapq.heappush(cola, (distancia, nodo_vesino))

    return visitados

grafo = {
    'entada':{'pocicion':(0,0),'ruta':[('sala', 1), ('cuarto_PB',1)]},
    'sala':{'pocicion':(1,1),'ruta':[('comedor',2),('escaleras',1.5)]},
    'cuarto_PB':{'pocicion':(1,0),'ruta':[]},
    'comedor':{'pocicion':(2,1),'ruta':[('baño_PB',2),('cocina',4)]},
    'baño_PB': {'pocicion':(2,0),'ruta':[]},
    'cocina':{'pocicion': (3,1),'ruta':[('cuarto_lavado',5),('patio_tracero',5)]},
    'cuarto_lavado':{'pocicion':(4,1),'ruta':[]},
    'patio_tracero':{'pocicion':(4,0),'ruta':[]},
    'escaleras':{'pocicion':(1,2),'ruta':[('planta_Alta',2.5)]},
    'planta_Alta':{'pocicion':(1.5,3),'ruta':[('cuarto_PA',9),('vestibulo',8),('cuarto_PA_2',10)]},
    'cuarto_Pa':{'pocicon':(0,2),'ruta':[]},
    'vestibulo':{'pocicion ':(1,3),'ruta':[]},
    'cuarto_PA_2': {'pocicion':(2,3),'ruta':[('baño_cuarto',12),('valcon',13)]},
    'baño_cuarto':{'pocicion':(3,4),'ruta':[]},
    'valcon':{'pocicion':(3,3),'ruta':[]},

    }
nodo_inicial = 'entada'
nodo_final = input(f'escoje un lugar de la casa:')


print(f'el camino mas corto es {voraz(grafo, nodo_inicial, nodo_final)}')