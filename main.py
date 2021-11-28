from src.utils1 import *
from src.utils2 import *
from utils4 import *

# print("Cambiar espacios por guiones")
# cad=input("Ingrese una frase: ")
# print(cambia_espacios(cad))

#print('Encontrar el subcampeón')
#puntajes = []
#while True:
#    puntaje = int(input('Ingrese el puntaje de un participante: '))
#    puntajes.append(puntaje)
#    cont = input('¿Desea ingresar más putajes? (s/n): ')
#    if cont == 'n':
#        break
#print('El subcampeón es:')
#subcampeon(puntajes)

'''
frase = input("Ingrese una frase:")
n=int(input("Ingrese un numero: "))
letra=input("Ingrese una letra: ")
print(modificar_string(frase,n,letra))
'''

#operaciones con Vectores
#vectores=vectorxyz()

#Creo carritos
'''
Carro1 = carrito(10)
Carro2 = carrito(10)
Carro3 = carrito(10)
Carro4 = carrito(10)
Carro5 = carrito(10)

#Creo el almacen
Wharehouse1 = Storage()
Wharehouse2 = Storage()

Wharehouse1.agregaCarrito(Carro1)
Wharehouse1.agregaCarrito(Carro2)
Wharehouse1.agregaCarrito(Carro3)

Wharehouse2.agregaCarrito(Carro4)
Wharehouse2.agregaCarrito(Carro5)

print(Wharehouse1.Ocupacion)
print(Wharehouse2.Ocupacion)



#Lsta de usuarios
ListUsers = Users()

Administra = UserCrate("Administrador","administrador@gmail.com","C:/avtr","A",Wharehouse1)
UsuarioComun = UserCrate("Marcelo Lopez","usuariocomun@gmail.com","C:/avtr","U",Wharehouse1)

UsuarioComun.muestra_carrito()


print(Wharehouse1.Almacen)
print(ListUsers.Usuarios)
print(Administra.uname)
print(Administra.email)
print(Administra.URiAvatar)
'''
palabra = "los espacios son"
sinespacios = cambia_espacios(palabra)

print(sinespacios)