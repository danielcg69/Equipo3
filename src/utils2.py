#opereciones con numeros complejos
class NumeroComplejo():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return f'{self.a}+{self.b}j'

    def sumar(self, otro):
        num_real = self.a + otro.a
        num_imag = self.b + otro.b
        return NumeroComplejo(num_real, num_imag)
    
    def restar(self, otro):
        num_real = self.a - otro.a
        num_imag = self.b - otro.b
        return NumeroComplejo(num_real, num_imag)
    
    def multiplicar(self, otro):
        num_real = self.a*otro.a - self.b*otro.b
        num_imag = self.a*otro.b + self.b*otro.a
        return NumeroComplejo(num_real, num_imag)
    
    # No me da del todo bien la division (le tuve que poner "0" al segundo número del return
    # porque en todos los casos que probé haciendo "otro.a / denominador_conjDenominador.b"
    # me daba error de ZeroDivision) 
    def dividir(self, otro):
        otro_conjugado = NumeroComplejo(otro.a, -otro.b)
        numerador_conjDenominador = self.multiplicar(otro_conjugado)
        denominador_conjDenominador = otro.multiplicar(otro_conjugado)
        return NumeroComplejo(numerador_conjDenominador.a/denominador_conjDenominador.a, 0)


#Operaciones con vectores
class vectorxyz:
    def __init__(self):
        self.x = int(input('Ingrese el valor de x: '))
        self.y = int(input('Ingrese el valor de y: '))
        self.z = int(input('Ingrese el valor de z: '))
        self.vector=[self.x, self.y, self.z]
        self.x1 = int(input('Ingrese el valor de x1: '))
        self.y1 = int(input('Ingrese el valor de y1: '))
        self.z1 = int(input('Ingrese el valor de z1: '))
        self.vector1=[self.x1, self.y1, self.z1]
        self.escalar=float(input('Ingrese el valor para escalar y dividir el primer vector: '))
        print('El primer vector es: ' + str(self.vector)) 
        print('El segundo vector es: ' + str(self.vector1))
        self.suma_vector_vector1()
        self.resta_vector_vector1()
        self.escal_vector()
        self.div_scalar()
      

    def vector(self):
        print('El vector es: ' + (self.vector()))
          
    def vector1(self):
        print('El vector es: ' + str(self.vector1))

    def suma_vector_vector1(self):
        suma = []
        for i in range(len(self.vector)):
            suma.append(self.vector[i] + self.vector1[i])
        print('La suma es: ' + str(suma))
    def resta_vector_vector1(self):
        resta = []
        for i in range(len(self.vector)):
            resta.append(self.vector[i] - self.vector1[i])
        print('La resta es: ' + str(resta))
    def escal_vector(self):
        escalar = []
        for i in range(len(self.vector)):
            escalar.append(round(self.vector[i] * self.escalar,2))
        print('El vector escalado es: ' + str(escalar))
    def div_scalar(self):
        div = []
        for i in range(len(self.vector)):
            div.append(round(self.vector[i] / self.escalar,2))
        print('El vector dividido es: ' + str(div))


#3- Crear una clase que represente una matriz de 3x3 dimensiones. 
# Tengan 3 metodos que permitan las operaciones matematicas basicas 
#(excluimos la division) (+ y - entre matrices, * solo por un vector).



#Crear una clase que represente al perfil usuario que ademas tenga una relacion (herencia) con estas
#dos clases: administrador y reportero (solo tiene lectura de datos). El usuario tiene objeto 
#carrito de compras. El administrador puede ver a todos los usuarios y lo que tenga adentro. 
#El reporter solo ve todos los carritos de compra.
#Leo J: 23-11-21

class PerfilUsuario:
    #atributo de clase
    
    def __init__(self,usuario,clave):
        self.usuario = usuario
        self.clave = clave

class Usuario(PerfilUsuario):
    #Atributos
    
    def carrito(self):
        self.carrito
        