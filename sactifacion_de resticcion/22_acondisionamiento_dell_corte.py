#programa 22 acondicionamiento

def solo(señal):
    #valores maximos y minimos
    max_valor = max(señal)
    min_valor = min(señal)

    solo =[(x-min_valor)/(max_valor-min_valor)for x in señal]

    return solo
i_señal=[10,20,30,40,50]
solo=solo(i_señal)
print(solo)
