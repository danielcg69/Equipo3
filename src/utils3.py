class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)


class Usuario:
    x=Carrito()
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        

    def __str__(self):
        return '{} <{}>'.format(self.nombre, self.email)
        
class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.admin=True

    def __str__(self):
        return '{} <{}> (admin)'.format(self.nombre, self.email)

class Report(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.report=True

    def __str__(self):
        return '{} <{}> (report)'.format(self.nombre, self.email)

    def reportar(self,Carrito):
        print('-----Listado Carrito------')
        print(Carrito)
        
        
    
#Lo siguinte es para probar el funcionamiento iria en el archivo main.py

chango=Carrito()
chango.agregar('pera')
chango.agregar('manzana')
chango.agregar('uva')
chango.agregar('naranja')

usuario=Usuario('Juan', 'juan@ppp.com')
admin=Administrador('Pedro', 'pedro@ppp.com')
usuario.x.agregar('pera')
reporter=Report(usuario, '  ')
reporter.reportar(chango)
usuario.reportar(chango)