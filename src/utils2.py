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