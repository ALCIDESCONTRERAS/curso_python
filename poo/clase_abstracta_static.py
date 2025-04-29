# Clase Abstracta: la plantilla o modelo de las clases que la hereden
from abc import ABC, abstractmethod

class Animal(ABC):
    #Atributo estático(Atributo de clase): va a estar disponible independientemente de las instancias
    cant_de_animales = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Animal.cant_de_animales += 1
    
    #un método abstracto de está forma obliga a las clases derivadas a implementar este comportamiento 
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    #Método de clase: es un método que se puede ejecutar desde la clase misma
    @classmethod
    def obtenerCantidadAnimales(cls):
        print(f'La cantidad actual de animales es: {cls.cant_de_animales}')
              
                    
class Perro(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace Guau Guau')
        
    def mover_cola(self):
        print(f'{self.nombre} está moviendo la cola')
        
class Gato(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace Miau Miau')
        
    def ronronear(self):
        print(f'{self.nombre} está ronroneando')
        
        
perrito = Perro('Manchita')
gatito = Gato('Pelusa')

perrito.mover_cola()
gatito.ronronear()

Animal.obtenerCantidadAnimales()