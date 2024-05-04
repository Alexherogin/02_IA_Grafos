#busqueda tabu
import random
def busqueda_tabu(lista, objetivo, tamano_tabu):
    #lista de elementos que no se pueden visitar
    tabu = []
    for i in range(tamano_tabu):
        #seleccionamos un elemento aleatorio de la lista
        elemento = random.choice(lista)
        #si el elemento no esta en la lista de tabu, lo agregamos
        if elemento not in tabu:
            tabu.append(elemento)
    #recorremos la lista
    for i in range(len(lista)):
        #si el elemento de la lista no esta en la lista de tabu, lo agregamos
        if lista[i] not in tabu:
            #si el elemento de la lista es igual al objetivo, lo retornamos
            if lista[i] == objetivo:
                return i
            #si el elemento de la lista no es igual al objetivo, lo agregamos a la lista de tabu
            else:
                tabu.append(lista[i])
                #si la lista de tabu tiene el tamaño maximo, eliminamos el primer elemento
                if len(tabu) == tamano_tabu:
                    tabu.pop(0)     