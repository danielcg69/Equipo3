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