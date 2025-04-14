class Contacto:
    contador = 0
    def __init__(self, nombre, telefono, email):
        Contacto.contador +=  1
        self.id_contacto = Contacto.contador
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        return f'id: {self.id_contacto}, Nombre: {self.nombre}, Telefono: {self.telefono}, Email: {self.email}'