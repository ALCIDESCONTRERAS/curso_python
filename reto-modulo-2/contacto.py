import re

class Contacto:
    contador = 0
    def __init__(self, nombre, telefono, email):
        if not Contacto.validar_nombre(nombre):
            raise ValueError(f"Nombre inválido: {nombre}")
        if not Contacto.validar_telefono(telefono):
            raise ValueError(f"Número de telefono inválido {telefono}")
        if not Contacto.validar_email(email):
            raise ValueError(f"Email inválido {email}")
        
        Contacto.contador +=  1
        self.id_contacto = Contacto.contador
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        return f'{self.id_contacto},{self.nombre},{self.telefono},{self.email}'

    @staticmethod
    def validar_nombre(nombre):
        regex = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ]{2,}([ -]?[A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$'
        return bool(re.match(regex, nombre))
    
    @staticmethod
    def validar_telefono(telefono):
        regex = r'^\+34\d{9}$|^\d{9}$'
        return bool(re.match(regex, telefono))
    
    @staticmethod
    def validar_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
        return bool(re.match(regex, email))