users = ['Ada', 'Sabrina', 'Noe', 'Virginia']

def obtener_chat_status(usuarias):
    counter = 0
    for personas in usuarias:
        counter += 1
        
    if counter == 0:
        return 'No hay nadie conectado'
    elif counter == 1:
        return 'nombre_usuaria_1 esta conectada'
    elif counter == 2:
        return 'nombre_usuaria_2 esta conectada'
    else:
        return 'NOMBRE_USUARIA_1, NOMBRE_USUARIA_2 y X persona(s) más están conectadas'
obtener_chat_status(users)

#ESTE ME SALIO TAMBIEN.!!!!!
        
        
        








'''
Crear una función obtener_chat_status que
tome como argumento una lista de strings usuarias
y devuelva un string con el status del chat. Las reglas son:

Para una usuaria, debe mostrar: NOMBRE_USUARIA_1 está conectada
Para dos usuarias, debe mostrar: NOMBRE_USUARIA_1 y NOMBRE_USUARIA_2 + están conectadas
Para más de dos usuarias, debe mostrar: NOMBRE_USUARIA_1, NOMBRE_USUARIA_2 y X persona(s)
más están conectadas
'''   