#busqueda tabu
import random 
def problemas(solucion):
    return sum (solucion)

def inicio (numeros):
    return [random.randint(0,50) for _ in range (numeros)]

def cambio_solus(solucion):
    index_1, indeX_2=random.sample(range(len(solucion)),2)
    solucion[index_1], solucion[indeX_2] = solucion[indeX_2], solucion[index_1]
    return solucion
   
#funcion de busqueda tabu
def tabu (interacciones,listas_tabu_1):
    #generar una solucion inicial
    solucion_m = inicio(10)
    #generar una lista tabu
    valor= problemas(solucion_m)
    lista_tabu = []
    for _ in range (interacciones):
        #generar una nueva solucion
        nuevo =[cambio_solus(solucion_m) for _ in range(10)]
        mejor_nuevo= min (nuevo, key=lambda x:(problemas(x)))
        
        if mejor_nuevo not in lista_tabu:
            solucion_m = mejor_nuevo
            valor= problemas(solucion_m)
            lista_tabu.append(mejor_nuevo)
        if len(lista_tabu) > listas_tabu_1:
            lista_tabu.pop(0)
    return solucion_m,valor
solucion_m, valor = tabu(interacciones=50, listas_tabu_1=5)
print(f'solucion encontrada : {solucion_m}')
print(f'valor es:  {valor}')

            
