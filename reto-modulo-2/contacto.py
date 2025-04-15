class Contacto:
    contador = 0
    def __init__(self, nombre, telefono, email):
        Contacto.contador +=  1
        self.id_contacto = Contacto.contador
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        return f'{self.id_contacto},{self.nombre},{self.telefono},{self.email}'
