#

def calcular_voi(v_actual,costo_inf,valor_inf,pe):
    informa=pe*valor_inf
    infoma_v=pe*v_actual
    adicion= informa-infoma_v
    voi=adicion-costo_inf
    return voi

v_actual =1000 # 
costo_inf = 2000 #

valor_inf = 12000 #
pe = 0.7
voi=calcular_voi(v_actual,costo_inf,valor_inf,pe)

print(voi)