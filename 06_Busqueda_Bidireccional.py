#Programa para la Busqueda Bidireccional

def Bidireccional(grafo, inicio, meta):
    #Se define la funcion de busqueda
    star = set()
    finish=set()
    cola_inico = [(inicio,[])]
    cola_fin = [(meta,[])]

    while cola_inico and cola_fin:
        if len(cola_inico)<=len(cola_fin):
            cola =cola_inico
            recorrido = star
        else:
            cola = cola_fin
            recorrido = finish
        estado, camino = cola.pop(0)
        if estado in recorrido:
            continue

        recorrido.add(estado)
        if estado == meta:
            return [camino + [n[0]for n in finish if n[0]!= meta]]
        for vecino, peso  in grafo.get(estado,{}).items():
            if vecino not in recorrido:
                cola.append((vecino, camino+[vecino]))
    return None

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

print('gracias por los datos :')
print('El camino mas corto es: ')
camino = Bidireccional(Jalisco, inicio, meta)
if camino:
    for c in camino:
        print(' -> '.join(c))
else:
    print('No hay camino entre ', inicio, 'y', meta)