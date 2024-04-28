#Busqueda inerativa  sera el siguiente codigo 

def Busqueda_Interativa(grafo, inicio,meta):
    recorrido = set()
    acumulado= [(inicio, [])]

    while acumulado:
        estado, camino = acumulado.pop()

        if estado in recorrido:
            continue

        recorrido.add(estado)

        if estado == meta:
            return camino
        for vecino, _ in grafo.get(estado,{}).items():
            if vecino not in recorrido:
                acumulado.append((vecino,camino+[estado]))
    return None

Jalisco = {
    'guadalajara':{'zapopan':10,'tlaquepaque':8,'tonala':10,'chapala':80,'ocotlan':100,'tlajomulco':28},
    'zapopan':{'guadalajara':10,'tlaquepaque':12},
    'tlaquepaque':{'guadalajara':8,'zapopan':12,'tlajomulco':20},
    'tonala':{'guadalajara':10,'tlaquepaque':20},
    'chapala':{'guadalajara':80,'tlajomulco':60},
    'ocotlan':{'guadalajara':100,'tlajomulco':85 },
    'tlajomulco':{'guadalajara':28,'chapala':60,'tlaquepaque':20},
    }
inicio=input('Escoja la ciudad de salida: ')
meta=input('Escoja el destino deciado: ')


print(Busqueda_Interativa(Jalisco,inicio,meta))