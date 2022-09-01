user_pax_ingresan = int (input('Ingrese cantidad de pax o personas'))
user_hab = int (input('Ingrese opcion de habitacion, para 2, para 3 o para 4 pax'))

a= 50 #HABITACIONS TOTALES DE 2 PAX
b = 30 #HABITACIONES TOTALES DE 3 PAX
c = 20 #HABITACIONES TOTALES DE 4 PAX


entrega_dispon_hab =  user_pax_ingresan / user_hab

pax_de_50 = 100
pax_de_30 = 90
pax_de_20 = 80
cuantas_hab_me_quedan_50 = user_pax_ingresan - pax_de_50
cuantas_hab_me_quedan_30 = user_pax_ingresan - pax_de_30
cuantas_hab_me_quedan_20 = user_pax_ingresan - pax_de_20


print('La cantidad de habitaciones disponibles son {0}'.format(entrega_dispon_hab))
print('Quedan disponibles habitaciones {1},{2},{3}'.format(cuantas_hab_me_quedan_50, cuantas_hab_me_quedan_30, cuantas_hab_me_quedan_20))






'''
def hab_disp(pax_de_50, pax_de_30, pax_de_20):
    if pax_de_50  <= 100 and == : #ENTRARIAN EN TOTAL 100 PAX EN ESTA OPCION
        print('Hay lugar')
    if pax_de_30  <= 90: #ENTRARIAN EN TOTAL 90 PAX EN ESTA OPCION
        print('Hay lugar')   
    if pax_de_20 <= 80: #ENTRARIAN EN TOTAL 80 PAX EN ESTA OPCION
        print('Hay lugar') 
    else:
        print('Que busque otra opcion de hotel') 
hab_disp(4, 6, 10)
'''