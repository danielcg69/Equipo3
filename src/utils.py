def cambia_espacios(cadena):
    for i in range(len(cadena)):
        if cadena[i]==" ":
            cadena=cadena.replace(" ","-")
    return cadena

def modificar_string(palabra, indice, letra):
    resultado = ''
    contador = 0
    for x in palabra:
        contador += 1
        if contador == indice:
            resultado += letra
        else: resultado += x
    return resultado

#Cambiar mayuscula por minuscula y minuscula por mayuscula
def cambiar_mayuscula(cadena):
    x=len(cadena)
    if x <=100:
        cadena=cadena.swapcase()
        return cadena
    else:
        return "No se puede cambiar cadena muy larga"

# Encontrar el subcampeón.
def subcampeon(puntajes):
    campeon = puntajes[0]
    for i in puntajes:
        if i > campeon:
            campeon = i
    subcampeon = puntajes[0]
    for i in puntajes:
        if campeon > i > subcampeon:
            subcampeon = i
    print(subcampeon)

#Capitalización primera letra nombre y apellido
def capitalizado(nombre, apellido):
    return(nombre.capitalize() +' '+  apellido.capitalize())

