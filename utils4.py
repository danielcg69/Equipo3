#from typing import ChainMap

#4- Crear una clase que represente al perfil usuario que ademas tenga una relacion (herencia) con estas dos clases:
#administrador y reportero (solo tiene lectura de datos).El usuario tiene objeto carrito de compras.El administrador puede ver 
# a todos los usuarios y lo que tenga adentro.El reporter solo ve todos los carritos de compra.

class carrito: #clase que representa a los carritos q son atributos de los usuarios
    capacidad = 0
    
    def __init__(self,tamaño) -> None:
        self.capacidad = tamaño
        self.carrito = []
    
    def AgregaItem(self,item):
        if (len(carrito) == self.capacidad):
            print("El carrito esta completo")
        else:
            self.carrito.append(item)
        
    def BorraItem(self,item):
        if len(carrito) == 0:
            print("El carrito no tiene ningún item")
        else:
            self.carrito.remove(item)

class Storage: #lista de los carritos de los usuarios. Es el almacén
    Almacen = [carrito]
    Ocupacion = 0
    def __init__(self) -> None:
        self.Almacen = [carrito]

    def cantidadItems(self) -> int:
        self.Ocupacion = len(self.Almacen)
        return self.Ocupacion
    
    def agregaCarrito(self,carrito) -> None:
        self.Almacen.append(carrito)
        self.Ocupacion=self.Ocupacion + 1
    
    def sacaCarrito(self,itm=carrito) -> None:
        self.Almacen.remove(itm)
        self.Ocupacion=self.Ocupacion - 1
    
    def __str__(self) -> str:
        cadena = self.Almacen
        return cadena + self.Ocupacion

class UserTemplate:  #clase abstracta
    Perfil=""
    
    def __init__(self,uname,email,URiAvatar) -> None:
         self.uname=uname
         self.email=email
         self.URiAvatar=URiAvatar
         
    def __str__(self) -> str:
        pass
        
    def muestra_carrito(self, uname) -> None:
        pass
    
    def muestra_usuarios(self, uname) -> None:
        pass
    
    def __str__(self) -> str:
        pass
    
class Users: #es la lista de usuarios
    Usuarios =[]
    
    def __init__(self) -> None:
        pass

    def AgregaUsuario(self,Usuarios) -> None:
        Usuarios.append((UserTemplate.uname,UserTemplate.email))
    
    def __str__(self,Usuarios) -> str:
        cadena= "Los usuarios son:" + " "
        for i in range(len(Usuarios)):
            cadena= cadena + Usuarios[i] + ", "
        return

class Admin(UserTemplate):
    Perfil = "A"
    
    def __init__(self, uname, email, URiAvatar, Stor:Storage) -> None:
        super().__init__(uname, email, URiAvatar)    

    def muestra_carritos(Stor) -> None:
       print("Los carritos contienen: ", Stor )
    
    def muestra_usuarios(self, list) -> None:
        print("Los usuarios son: " ,list )
    
    def __str__(self) -> str:
        return super().__str__()
    
class Reporter(UserTemplate):
    Perfil = "R"
    
    def __init__(self, uname, email, URiAvatar, Stor:Storage) -> None:
        super().__init__(uname, email, URiAvatar)
    
    def muestra_carrito(self, Stor) -> None:
        print("Los carritos contienen: ", Stor )
    
    def muestra_usuarios(self) -> None:
        print ("Función no permitida para el tipo de usuario")

    def __str__(self) -> str:
        return super().__str__()
    
class Usuario(UserTemplate):
    Perfil = "U"
    Ucarrito = carrito(10)
    
    def __init__(self, uname, email, URiAvatar,stor:Storage) -> None:
        super().__init__(uname, email, URiAvatar)
        stor.agregaCarrito(self.Ucarrito)
    
    def muestra_carrito(self) -> None:
       # return super().muestra_carrito(uname)
       print("El carrito contiene: " + "{}", self.Ucarrito)
    
    def muestra_usuarios(self) -> None:
       #return super().muestra_usuarios()
       print ("Soy el Usuario: " + self.uname)
    
    def __str__(self) -> str:
        return super().__str__()
    
class UserCrate(UserTemplate):
    def __init__(self, uname, email, URiAvatar,type,stor) -> None:
        self.uname=uname
        self.email=email
        self.URiAvatar=URiAvatar
        if (type=="A"):   
            Admin(uname,email,URiAvatar,stor)
        elif(type=="R"):
            Reporter(uname,email,URiAvatar,stor)
        elif(type=="U"):
            Usuario(uname,email,URiAvatar,stor)
        else:
            print("Tipo de usuario incorrecto")
