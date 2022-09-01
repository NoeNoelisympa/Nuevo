numeros = [0, 3, 5, 88, 10, 44, 103]
def contiene(numero, numeros):
    for elemento in numeros:
        if numero == elemento:
            return True
    
    return False        
contiene(103, numeros)

#ASI SI ME SALIO DE DOS FORMAS.

numeros = [0, 3, 5, 88, 10, 44, 103]
numero = int(input('Ingrese el numero que quiere encontrar'))
def contiene(numero, numeros):
    for elemento in numeros:
        if elemento == numero:
            return True
        
    return False
contiene(numero, numeros)

'''ASI DE ESTA FORMA NO ME SALIO.
mi_lista = [0, 3, 5, 88, 10, 44, 103]
numero = int(input('Ingrese el numero que quiere encontrar'))
def contiene(numero, mi_lista):
    for elemento in range(len(mi_lista)):
        if numero == elemento:
            return True
        
    return False
contiene(numero, numeros)
'''