#BUsqueda de Haz Locoal

import random
def problema (x):
    return x**2

vueltas =10
recorridos = 100
rango= (-10,10)

def cantidad():
    return[random.uniform(rango[0],rango[1]) for _ in range(vueltas)]

def E_cantidad(cant):
    return sum (problema(x) for x in cant) /vueltas

def buscar(vueltas,recorridos,rango):
    actual = cantidad()
    mejor_valor = E_cantidad(actual)
    for _ in range(recorridos):
        valor = E_cantidad(actual)
        if valor < mejor_valor:
            mejor_valor = valor
            actual = [x + random.uniform(-0.1,0.1) for x in actual]
    return mejor_valor
   


mejor_solu = buscar(vueltas,recorridos,rango)
    



print(f'solucion encontradaes : {mejor_solu}')

    
        
        

