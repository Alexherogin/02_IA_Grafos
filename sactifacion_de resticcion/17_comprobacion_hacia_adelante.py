#

def sum_plus(datos):
    valor_suma =0
    for i in datos:
        valor_suma += i

    return valor_suma 
datos = [0x10,0x20,0x30,0x40,0x50]
res=sum_plus(datos)
print(f'{res} byts')
