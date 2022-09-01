
'''facil = 3
normal = 5
dificil = 10 #puntos

suma_examenes = float(input('Ingrese su puntaje de los examenes en total'))
cantidad_examenes = 3

media_aprobar = 6 #puntos
total_aprobar = 18 #puntos

puntaje = suma_examenes / cantidad_examenes

def calcular_puntaje(media_aprobar, puntaje):
    return media_aprobar - puntaje
calcular_puntaje(media_aprobar, puntaje)
'''
    
#ARREGLAR
'''
facil = 3
normal = 5
dificil = 10 #puntos

examen_facil = float(input('Ingrese su puntaje de los examenes en total'))
examen_normal = float(input('Ingrese su puntaje de los examenes en total'))
examen_dificil = float(input('Ingrese su puntaje de los examenes en total'))

def calcular_puntaje(facil, normal, dificil):
    if examen_facil + examen_normal + examen_dificil == 18 #puntos:
        return 'Aprobado'
    else:
        return 'Tiene que mejorar'
calcular_puntaje(facil, normal, dificil)
'''


facil = 3
normal = 5
dificil = 10 #puntos

examen_facil = float(input('Ingrese su puntaje de los examenes en total'))
examen_normal = float(input('Ingrese su puntaje de los examenes en total'))
examen_dificil = float(input('Ingrese su puntaje de los examenes en total'))

def calcular_puntaje(facil, normal, dificil):
    if examen_facil >= 2:
        return True
    if examen_normal >= 4:
        return True
    if examen_dificil == 10: #puntos
        return 'Aprobado'
    else:
        return False
calcular_puntaje(1, 3, 10)
