class Pelicula():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def escribir_pelicula(self):
        return f"Pelicula: {self.nombre}"