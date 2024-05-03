#Busqueda inerativa  sera el siguiente codigo 

def Busqueda_Interativa(grafo, inicio,meta): #se define la funcion de busqueda inerativa
    recorrido = set()
    acumulado= [((inicio, 0), [inicio])]

    while acumulado:#mientras la lista de acumulado no este vacia
        (estado, distancia), camino = acumulado.pop()

        if estado in recorrido:
            continue    #si el estado ya se encuentra en el recorrido se continua

        recorrido.add(estado) #se agrega el estado a la lista de recorrido

        if estado == meta:
            return camino, distancia #si se encuentra la meta se retorna el camino y la distancia
        for vecino, peso in grafo.get(estado,{}).items():
            if vecino not in recorrido:
                acumulado.append(((vecino,distancia+ peso ),camino+[estado]))#se agrega el vecino a la lista de acumulado
    return None #si no se encuentra la meta se retorna None



Jalisco = {
    'guadalajara':{'zapopan':10,'tlaquepaque':8,'tonala':10,'chapala':80,'ocotlan':100,'tlajomulco':28},
    'zapopan':{'guadalajara':10,'tlaquepaque':12},
    'tlaquepaque':{'guadalajara':8,'zapopan':12,'tlajomulco':20},
    'tonala':{'guadalajara':10,'tlaquepaque':20},
    'chapala':{'guadalajara':80,'tlajomulco':60},
    'ocotlan':{'guadalajara':100,'tlajomulco':85 },
    'tlajomulco':{'guadalajara':28,'chapala':60,'tlaquepaque':20},
    }#grafo de ejemplo
inicio=input('Escoja la ciudad de salida: ')#el usuario ingresa el inicio y meta
meta=input('Escoja el destino deciado: ')


print(Busqueda_Interativa(Jalisco,inicio,meta)) #se imprime el resultado de la busqueda inerativa