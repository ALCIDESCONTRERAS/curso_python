from servicio_pelicula import ServicioPelicula

class CatalogoPelicula():
    salir = False
    def __init__(self):
        self.servicio_peliculas = ServicioPelicula()
          
    def catalogo_pelicula(self):
        salir = False
        while not salir:
            try:
                opcion = self.mostrar_opciones()
                salir = self.ejecutar_opcion(opcion)
            except ValueError:
                print("Introduce un numero válido")
            except Exception as e:
                print(f"Se produjo un error {e}")
        
    def mostrar_opciones(self):
        print('''Menú:
              1. Agregar pelicula
              2. Listar peliculas
              3. Eliminar catalogo de Peliculas
              4. Salir
              ''')
        return int(input("Elige una opción(1-4): "))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.servicio_peliculas.agregar_pelicula()
        elif opcion == 2:
            self.servicio_peliculas.listar_peliculas()
        elif opcion == 3:
            self.servicio_peliculas.eliminar_peliculas()
        elif opcion == 4:
            print("Salimos del Programa")
            return True
        else:
            print("Opción invalida, eleije una opción entre 1 y 4")
            
            
#Programa principal
if __name__ == "__main__":
    catalogo_peli = CatalogoPelicula()
    catalogo_peli.catalogo_pelicula()