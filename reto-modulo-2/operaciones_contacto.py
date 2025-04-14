from contacto import Contacto

class OperacionesContacto:
    def __init__(self):
        self.archivo_contacto = "contactos.txt"
        
    def crear_contacto(self):
        try:                
            nombre = input('Escribe el nombre del contacto: ')
            telefono = input('Escribe el numero de telefono: ')
            email = input('Escribe dirección de correo electrónico: ')
            contacto = Contacto(nombre, telefono, email)
            with open(self.archivo_contacto, 'a', encoding='utf8') as archivo:
                archivo.write(f'{contacto}\n')
        except Exception as e:
            print(f'Ocurrió un error al crear contacto: {e}')
            
    def listar_contactos(self):
        print('------Lista de Contactos--------')
        with open(self.archivo_contacto, 'r') as archivo:
            print(archivo.read())
            
    
    
    
if __name__ == '__main__':
    operaciones = OperacionesContacto()
    operaciones.listar_contactos()