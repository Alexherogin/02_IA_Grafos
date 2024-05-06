#programa23guncion utilidad

def par(numero):
    return numero %2 ==0
def primo(numero):
    if numero <=1:
        return False
    if numero <= 3 :
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i = i + 6
        return True
def factor(numero):
    if numero == 0:
        return 1
    return numero * factor(numero -1)
def listas(lista):
    return ','.join(lista)

def palidro(cadena):
    cadena =cadena.replace('','').lower()
    return cadena== cadena[::-1]

if __name__ =='__main':
    print(par(2))
    print(primo(2))
    print(factor(5))
    print(listas([1,2,3,4,5]))
    print(palidro('oso'))
    