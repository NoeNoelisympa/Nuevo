nombre = input( 'Ingrese su nombre')
apellido = input('Ingrese su apellido')
edad = str (int (input('Ingrese su edad')))
nacionalidad = input('Ingrese su nacionalidad')
documento = str (int (input('Ingrese su documento')))
mensaje = 'Nuevo usuario agregado al sistema'
mensaje2 = mensaje + nombre + apellido + edad + nacionalidad + documento
print(mensaje2)