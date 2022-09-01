edad = int(input('Ingrese su edad'))

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    if edad < 18:
        return False
es_mayor_de_edad(edad)