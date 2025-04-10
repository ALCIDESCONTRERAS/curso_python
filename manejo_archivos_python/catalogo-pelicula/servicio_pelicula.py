from pelicula import Pelicula
import os

class ServicioPelicula():
    def __init__(self):
        self.nombre_archivo = "pelicula.txt"        
        
    def agregar_pelicula(self):
        peli_usuario = input("Escribe el nombre de la pelicula: ")
        pelicula = Pelicula(peli_usuario)
        with open(self.nombre_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")
        print("Pelicula agregada correctamente")    
            
    def listar_peliculas(self):
        print("---Lista de peliculas---")
        with open(self.nombre_archivo, "r", encoding="utf8") as archivo:
            print(archivo.read())
            
    def eliminar_peliculas(self):
        os.remove(self.nombre_archivo)
        print("Archivo eliminado correctamente")
    