
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
# Esta versión está basada en la de Leo con unas pequeñas modificaciones, Ibi 28-11-21
def subcampeon(puntajes):
    puntajes.sort(reverse = True)
    subcampeon = puntajes[0]
    for i in puntajes:
        if puntajes[0] > i:
            subcampeon = i
            break
    print(subcampeon)
    
#Versión Leo Jota 25-11-21
def subcampeon_LJ(puntajes):
    
    puntajesord = puntajes.sort() #El método sort() retorna None, Ibi 28-11-21
    
    subcampeon = puntajesord[0] #Acá me tira este error: TypeError: 'NoneType' object is not subscriptable, Ibi 28-11-21
    for i in len(puntajesord):
        if puntajesord[0] > puntajesord[i]:
            subcampeon = puntajesord[i]
            return subcampeon

#Extra A
def imprimir_triangulo(numero):
    for x in range(numero+1):
        print(str(x)*x)
        
        
#Extra B (falta hacer)
def car_mas_usados(nombre):
    nombre = nombre.lower()
    #Creo una lista y almaceno los carácteres únicos del string.
    car_list = []
    for i in nombre:
        if i not in car_list and i != ' ':
            car_list.append(i)
    #Creo una lista paralela que almacena la cantidad de veces que aparece cada carácter
    #del string.
    cant_list = []
    for i in car_list:
        cant_list.append(nombre.count(i))
    #A partir de acá hago bardo:
    #Creo una copia de la lista de cantidades y la ordeno de menor a mayor, con tal de que queden
    #los más usados al principio.
    mas_usados = cant_list.copy()
    mas_usados.sort(reverse=True)
    #Creo una lista en donde voy a almacenar los carácteres más usados.
    car_mas_usados = []
    for i in range(3):
        car_mas_usados.append(car_list[cant_list.index(mas_usados[i])])
        car_list.pop(cant_list.index(mas_usados[i]))
        cant_list.pop(cant_list.index(mas_usados[i]))
    #Imprimo el top 3 y la cantidad de veces que aparecen.
    print(f'{car_mas_usados[0]}: {mas_usados[0]}')
    print(f'{car_mas_usados[1]}: {mas_usados[1]}')
    print(f'{car_mas_usados[2]}: {mas_usados[2]}')