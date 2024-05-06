#

import random

paso = [(0,0),(0,1),(1,0),(1,1)]
accion = ['adelante','atras']

grafo = {
    (0,0):-1,
    (0,1): 10,
    (1,0):-1,
    (1,1): 1
}

move = {
    (0, 0): {"adelante": (0, 1), "derecha": (1, 0)},
    (0, 1): {"adelante": (1, 1), "derecha": (0, 0)},
    (1, 0): {"adelante": (1, 1), "derecha": (0, 0)},
    (1, 1): {"adelante": (1, 0), "derecha": (0, 1)},
}

valor ={paso:0 for paso in paso}

poli = {paso: random.choice(accion)for paso in paso}
des= 0.9

for _ in range(100):
    N_valor= {}
    for paso in paso:
        accion=poli[paso]
        N_pasos= move[paso][accion]
        suma = grafo[paso]+des*valor[N_pasos]
        N_valor[paso]=suma

    valor=N_valor
    #max_valor= 0
    for paso in paso:
        M_accion=None #move[paso][accion]
        max_valor= float('-inf')
        N_pasos=move[paso][accion]
        val= grafo[paso]+des*valor[N_pasos]
        if val > max_valor:
            max_valor= val
        M_accion = accion
        poli[paso]=M_accion
print('politica optima: ')
for paso,accion in poli.items():
    print(f'los pasos fue{paso}: tomar la accion{accion}')
            

            
