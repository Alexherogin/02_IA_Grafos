# practica de busqueda por profundida limitada se busco una manera diferente a la de la busqueda por profundidad
# en la cual se busca el nodo en el arbol y se le da una profundidad limite en lugar de una lista para el grafo

class nodo:#
    def __init__(self,valor ) -> None:
        self.valor = valor 
        self.izq = None 
        self.der = None

def busqueda_profundidad_limitada(nodo, objeto,pLimite,profundo=0):  #funcion para buscar el nodo en el arbol con diferentes condicionales
    if nodo == None:    # si el nodo es nulo se retorna falso
        return False
    if nodo.valor == objeto:   
        return True
    if profundo > pLimite:
        return False
    if busqueda_profundidad_limitada(nodo.izq,objeto,pLimite,profundo+1):# se busca en el arbol de forma recursiva
        return True
    if busqueda_profundidad_limitada(nodo.der,objeto,pLimite,profundo+1):#
        return True
raiz=nodo(1)  # raiz para generar la busquede limitada
raiz.izq=nodo(2)
raiz.der=nodo(3)
raiz.izq.izq=nodo(4)
raiz.izq.der=nodo(5)
raiz.der.der=nodo(6)
raiz.der.izq=nodo(7)
raiz.izq.izq.izq=nodo(8)
raiz.izq.izq.der=nodo(9)
raiz.der.der.der=nodo(10)
raiz.izq.izq.izq.izq=nodo(11)
raiz.izq.izq.izq.der=nodo(12)

objeto= int(input('ingresa el nodo a bucar del 1 al 12: '))# se ingresa el nodo a buscar
pLimite = int(input('seleccione la profundidad de busqueda 0 a 4 : '))#
Res= busqueda_profundidad_limitada(raiz,objeto,pLimite )# se llama la funcion para buscar el nodo
if Res:
    print(f'el nodo si esta {objeto} dentro de la profundidad {pLimite}')
else: 
    
    print(f'el nodo no esta {objeto} dentro de la profundidad {pLimite}')