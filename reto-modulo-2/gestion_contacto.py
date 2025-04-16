from contacto import Contacto
import os.path

class OperacionesContacto:
    archivo_contacto = "contactos.txt"
    
    def __init__(self):
        self.contactos = []
        if os.path.isfile(self.archivo_contacto):
            self.contactos = self.obtener_contactos()
        else:
            self.cargar_contactos()
    
    def cargar_contactos(self):
        contactos_iniciales = [
            Contacto('Facundo', '692916064', 'facuscrollini@gmail.com'),
            Contacto('Roberto', '722625623', 'roberto@gmail.com'),
            Contacto('Miguel', '635658156', 'miguelangel@gmail.com')
        ]        
        self.contactos.extend(contactos_iniciales)
        
        with open(self.archivo_contacto, 'w', encoding='utf8') as archivo:
            for contacto in self.contactos:
                archivo.write(f'{contacto}\n')    
        
    def obtener_contactos(self):
        contactos = []
        try:
            with open(self.archivo_contacto, 'r', encoding='utf8') as archivo:
                for linea in archivo:
                    id, nombre, telefono, email = linea.strip().split(',')
                    contacto = Contacto(nombre, telefono, email)
                    contactos.append(contacto)
        except Exception as e:
            print(f'Ocurrió un error: {e}')
        
        return contactos
    
    def crear_contacto(self):
        try:                
            nombre = input('Escribe el nombre del contacto: ')
            telefono = input('Escribe el numero de telefono: ')
            email = input('Escribe dirección de correo electrónico: ')
            contacto = Contacto(nombre, telefono, email)
            with open(self.archivo_contacto, 'a', encoding='utf8') as archivo:
                archivo.write(f'{contacto}\n')
            self.contactos.append(contacto)
            print("Contacto Agregado!!!")
        except Exception as e:
            print(f'Ocurrió un error al crear contacto: {e}')
                     
    def eliminar_contacto(self):
        try:
            id_usuario = int(input('Escribe el id del contacto: '))
            contacto_encontrado = None
                                
            for contacto in self.contactos:
                if contacto.id_contacto == id_usuario:
                    contacto_encontrado = contacto
                    
            if contacto_encontrado:
                self.contactos.remove(contacto_encontrado)
                with open(self.archivo_contacto, 'w', encoding='utf8') as archivo:
                    for contacto in self.contactos:
                        archivo.write(f'{contacto}\n')
                print(f'Contacto con el id {id_usuario} eliminado correctamente!!!')
            else:
                print(f'No se encontró el contacto con el id {id_usuario}')            
        except ValueError:
            print(f'Escriba un número válido')
        except Exception as e:
            print(f'Ocurrió un error al eliminar el contacto: {e}')
                  
    def actualizar_contacto(self):
        try:
            id_usuario = int(input('Escribe el id del contacto a actualizar: '))
            contacto_encontrado = None
            
            for contacto in self.contactos:
                if contacto.id_contacto == id_usuario:
                    contacto_encontrado = contacto
                    
            if contacto_encontrado:
                nuevo_nombre = input('Escribe el nuevo nombre del contacto: ')
                nuevo_telefono = input('Escribe el nuevo telefono del contacto: ')
                nuevo_email = input('Escribe el nuevo email del contacto: ')
               
                if nuevo_nombre:
                   contacto_encontrado.nombre = nuevo_nombre | contacto_encontrado.nombre
                if nuevo_telefono:
                    contacto_encontrado.telefono = nuevo_telefono | contacto_encontrado.telefono
                if nuevo_email:
                    contacto_encontrado.email = nuevo_email | contacto_encontrado.email
                    
                with open(self.archivo_contacto, 'w', encoding='utf8') as archivo:
                    for contacto in self.contactos:
                        archivo.write(f'{contacto}\n')
                
                print('Contacto actualizado correctamente!!!')
                
            else:
                print(f'Contacto con id {id_usuario} no se encontró')
                
                
        except ValueError:
            print(f'Escriba un número válido')
        except Exception as e:
            print(f'Ocurrió un error al actualizar el contacto: {e}')
            
    def buscar_contactos(self):
        try:
            nombre_usuario = input('Escribe el nombre el contacto: ').lower()
            encontrado = False
            
            for contacto in self.contactos:
                if nombre_usuario in contacto.nombre.lower():
                    print(f'Id: {contacto.id_contacto}, Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Email: {contacto.email}')
                    encontrado = True
            if not encontrado:
                print('Contacto no encontrado')
                
        except Exception as e:
            print(f'Ocurrió un error a buscar contacto: {e}')
    
    def listar_contactos(self):
        print('------------------Lista de Contactos-----------------------')
        for contacto in self.contactos:
            print(f'Id: {contacto.id_contacto}, Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Email: {contacto.email}')
            
    def eliminar_archivo_contacto(self):
        os.remove(self.archivo_contacto)
        print("Archivo de contactos eliminado!!")
        
        
if __name__ == '__main__':
    operacion = OperacionesContacto()
    operacion.buscar_contactos()