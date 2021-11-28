
    #No hace falta el for. la función replace cambia todos los espacios q encuentra por el guión
#    return cadena.replace(" ","-")

def cambia_espacios(cadena):
    cadAux = ""
    
    for i in range(len(cadena)):
       if cadena[i] == " ":
            cadAux += "-"
       else:
            cadAux += cadena[i] 
    
    return cadAux


#Que ejercicio es esta función? (Leo J), pone letra en la posición indicada por indice
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
#Bien!! --> Leo J
def cambiar_mayuscula(cadena):
    x=len(cadena)
    if x <=100:
        cadena=cadena.swapcase()
        return cadena
    else:
        return "No se puede cambiar cadena muy larga"

#Capitalización primera letra nombre y apellido
#Bien! --> Leo J
def capitalizado(nombre, apellido):
    return(nombre.capitalize() +' '+  apellido.capitalize())
      

# Encontrar el subcampeón.
# Leo J: para mi no funciona. Ver otras opción 23-11-21
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
    
#Versión Leo Jota 25-11-21
def subcampeon_LJ(puntajes):
    
    puntajesord = puntajes.sort()
    
    subcampeon = puntajesord[0]
    for i in len(puntajesord):
        if puntajesord[0] > puntajesord[i]:
            subcampeon = puntajesord[i]
            return subcampeon

#Extra A
def imprimir_triangulo(numero):
    for x in range(numero+1):
        print(str(x)*x)
        
        
#Extra B (falta hacer)