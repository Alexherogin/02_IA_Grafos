
from constraint import Problem
problema = Problem()
#Definir variables
letras = ['a','b','c','d']
colores = ['rojo','verde','negro']
#Definir dominios
for abcd in letras:
    problema.addVariables(abcd,colores)

#Definir restricciones
problema.addConstraint(lambda a,b:a!=b, ('a','b'))
problema.addConstraint(lambda b,c : b!=c, ('b','c'))
problema.addConstraint(lambda c,d : c!=d, ('c','d'))
#Resolver
solucion = problema.getSolutions()
for s in solucion:
    print(s)
