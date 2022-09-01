user_product_1 = input('Ingrese su primer producto a comprar')
user_product_2 = input('Ingrese su segundo producto a comprar')
user_product_3 = input('Ingrese su tercer producto a comprar')

product_1 = 500
product_2 = 800
product_3 = 1200
suma_product = product_1 + product_2 + product_3

user_cuotas = int (input('Ingrese cantidad de cuotas'))

cuotas_3_inicial = suma_product / 3
interes_cuota_3 = ((suma_product * 15) / 100)
cuotas_3 = cuotas_3_inicial + interes_cuota_3

cuotas_6_inicial = suma_product / 6
interes_cuota_6 = ((suma_product * 20) / 100)
cuotas_6 = cuotas_6_inicial + interes_cuota_6

cuotas_12_inicial = suma_product / 12
interes_cuota_12 = ((suma_product * 25) / 100)
cuotas_12 = cuotas_12_inicial + interes_cuota_12

def cuot_3(cuotas_3):
    if cuotas_3 == cuotas_3:
        return True
    else:
        return False
print('Usted compro los productos en tres cuotas por el valor de')
print(cuotas_3)

def cuot_2(cuotas_6):
    if cuotas_6 == cuotas_6:
        return True
    else:
        return False
print('Usted compro los productos en seis cuotas por el valor de')
print(cuotas_6)

def cuot_12(cuotas_12):
    if cuotas_12 == cuotas_12:
        return True
    else:
        return False
print('Usted compro los productos en doce cuotas por el valor de')
print(cuotas_12)

# ESTA BIEN.
#Ingrese su primer producto a comprar Perfume
''' EJEMPLO
Ingrese su segundo producto a comprar Lysoform
Ingrese su tercer producto a comprar Coleccion Skip
Ingrese cantidad de cuotas 3
Usted compro los productos en tres cuotas por el valor de
1208.3333333333335
Usted compro los productos en seis cuotas por el valor de
916.6666666666667
Usted compro los productos en doce cuotas por el valor de
833.3333333333334
'''