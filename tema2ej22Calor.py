temperatura = float(input('Ingrese la temperatura actual'))
calor = 'Hace calor'
frio = 'Hace frio'

def hace_calor(temperatura):
    if temperatura >= 18:
        return calor
    if temperatura < 18:
        return frio
hace_calor(temperatura)