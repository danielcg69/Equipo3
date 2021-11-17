def cambia_espacios(cadena):
    for i in range(len(cadena)):
        if cadena[i]==" ":
            cadena=cadena.replace(" ","-")
    return cadena
