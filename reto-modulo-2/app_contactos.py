from gestion_contacto import OperacionesContacto

class AppContactos:
    def __init__(self):
        self.operaciones_contacto = OperacionesContacto()
    
    def ejecutar_opciones(self):
        opcion = None
        try:
            while opcion != 6:
                print('------------Menú de opciones para la gestión de contactos----------')
                print('''Menú:
                    1. Mostrar contactos
                    2. Crear contactos
                    3. Actualizar contactos
                    4. Eliminar contactos
                    5. Buscar contacto
                    6. Salir''')
                opcion = int(input('Escibe una opción (1-5): '))
                
                if opcion == 1:
                    self.operaciones_contacto.listar_contactos()
                elif opcion == 2:
                    self.operaciones_contacto.crear_contacto()
                elif opcion == 3:
                    self.operaciones_contacto.actualizar_contacto()
                elif opcion == 4:
                    self.operaciones_contacto.eliminar_contacto()
                elif opcion == 5:
                    self.operaciones_contacto.buscar_contactos()
                else:
                    print('Elije una opcion entre el 1 y 6')
            else:
                print('Vuelve pronto!!!')
        except ValueError:
            print('Elije una opción correcta')
        except Exception as e:
            print(f'Ocurrió un error: {e}')
        
        
if __name__ == '__main__':
    app = AppContactos()
    app.ejecutar_opciones()
        

# operaciones_contacto = OperacionesContacto()
# opcion = None
# try:
#     while opcion != 5:
#         print('------------Menú de opciones para la gestión de contactos----------')
#         print('''Menú:
#             1. Mostrar contactos
#             2. Crear contactos
#             3. Actualizar contactos
#             4. Eliminar contactos
#             5. Salir''')
#         opcion = int(input('Escibe una opción (1-5): '))
        
#         if opcion == 1:
#             operaciones_contacto.listar_contactos()
#         elif opcion == 2:
#             operaciones_contacto.crear_contacto()
#         elif opcion == 3:
#             operaciones_contacto.actualizar_contacto()
#         elif opcion == 4:
#             operaciones_contacto.eliminar_contacto()
#     else:
#         print('Vuelve pronto!!!')
# except ValueError:
#     print('Elije una opción correcta')
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

        
