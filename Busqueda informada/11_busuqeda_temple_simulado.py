# codigo busqueda de temple simulado

import math
import random

def problema(x):
    return x**2 + 4*x
def busqueda_simu(problema,T_inicial,Tenf,recorrido):
    MS= random.uniform(-10,10)
    MV= problema(MS)
    actual=T_inicial

    for _ in range(recorrido):
        Ns =MS+random.uniform(-0.1,0.1)
        valor = problema(Ns)

        if valor>MV or random.random()<math.exp((valor-MV)/actual):
            MS=Ns
            MV=valor

        actual*=Tenf
    return MS,MV

if __name__ == "__main__":
    T_inicial= 100.0
    Tenf= 0.99

    recorrido= 1000

    MS,MV= busqueda_simu(problema,T_inicial,Tenf,recorrido)
    print(f'solucion encontrada es = {MS}, y su valor es: {MV}')