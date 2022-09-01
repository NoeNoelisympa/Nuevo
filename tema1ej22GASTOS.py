dinero_disponible = int (input('Seleccione cantidad de dinero disponible'))

user_monto_gas = int (input('Ingrese cantidad a pagar de gas'))
user_monto_luz = int (input('Ingrese cantidad a pagar de luz'))
user_monto_agua = int (input('Ingrese cantidad a pagar de agua'))

user_dinero_ingresado = int (input('Ingrese la cantidad de dinero ingresado anteriormente'))

# LO QUE LE QUEDA
no_ingresados = dinero_disponible - user_dinero_ingresado

# INGRESA LAS OPCIONES DE LO QUE QUIERE PAGAR
gas = str (input('Ingrese opcion Gas si quiere pagar Gas'))
luz = str (input('Ingrese opcion Luz si quiere pagar Luz'))
agua = str (input('Ingrese Opcion agua si quiere pagar agua'))

mi_diccionario = {gas:user_monto_gas, luz :user_monto_luz, agua:user_monto_agua}

total_service = mi_diccionario


a = gas + luz
b = gas + agua
c = gas
d = luz + agua
e = luz
f = agua
g = gas + luz + agua

a_1 = user_monto_gas + user_monto_luz
b_1 = user_monto_gas + user_monto_agua
c_1 = user_monto_gas
d_1 = user_monto_luz + user_monto_agua
e_1 = user_monto_luz
f_1 = user_monto_agua
g_1 = user_monto_gas + user_monto_luz + user_monto_agua


def queda_pagar(a_1, b_1, c_1, d_1, e_1, f_1, g_1):
    for pagar in range(0, 6):
        if pagar == a_1:
            return f_1
        elif pagar == b_1:
            return e_1
        elif pagar == c_1:
            return a_1
        elif pagar == d_1:
            return c_1
        elif pagar == e_1:
            return b_1
        elif pagar == f_1:
            return a_1
        elif pagar == g_1:
            return True
        break

queda_pagar(a_1, b_1, c_1, d_1, e_1, f_1, g_1)

print('Usted le queda por pagar:', queda_pagar)
print('Usted pago los siguientes servicios:{}'.format(total_service))
print('Y le queda disponible de dinero: {}'.format(no_ingresados))



# EJERCICIO GASTOS
# 0 seria total_service
# 1 seria dinero_queda
# 2 seria servicios_ingresados
#print('Quedan por ingresar {0}'.format(servicios_ingresados)

