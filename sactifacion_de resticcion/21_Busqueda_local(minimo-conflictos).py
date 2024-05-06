#codido 21 busqueda local

import random

def star(n):
    return[random.randint(0,n-1)for _ in range(n)] 

def numeros (estado,index):
    caso = 0
    for i in range(len(estado)):
        if estado[i] != index:
            caso += 1
    return caso
def caso_minimo(csp,pasos_total=1000):
    estado = star(n)
    for _ in range(pasos_total):
        caso_plus =[ i for i in range(n) if numeros(estado, i)>0 ]
        if not caso_plus:
            return estado
        camino =random.choice(caso_plus)
        valor_caso = float('inf')
        caso_dep = estado[camino]
        for desp in range(n):
            if desp!= estado[camino]:
                estado[camino] = desp
                contador = numeros(estado,camino)
                if contador < valor_caso:
                    valor_caso = contador
                    caso_dep= desp
        estado[ camino]= caso_dep
    return None
def res (estado):
    for row in estado: 
        for col in range(len(estado)):
            if col ==estado[row]:
                print('Q', end=' ')
            else:
                print('-', end=' ')
        print()

if __name__ == '__main__':
    n = int(input('n: '))
    solucion = caso_minimo (range(n))
    if solucion:
        print('Solucion:')
        res(solucion)
    else:
        print('No hay solucion')