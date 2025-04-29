class Producto:
    def __init__(self, nombre=None, cantidad=None, precio=None, categoria=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
        
    def __str__(self):
        return f'{self.nombre}, {self.cantidad}, {self.precio}, {self.categoria}'
