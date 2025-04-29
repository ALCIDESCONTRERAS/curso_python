#Clase: es una plantilla que define caracteristicas y comportamientos de objetos
class Robot:
    #Constructor: es un metodo especial que se ejecuta al crar una instancia y permite inicializar los atributos
    #Self se refiere a la instacia específica
    def __init__(self, nombre, tipo):
        #Atributos o caracteristicas
        self.nombre = nombre
        self.tipo = tipo
        
    #Metodo es una funcion que define el comportamiento o acción de un objeto
    def saludar(self):
        print(f'Hola soy {self.nombre} y soy un robot locaso')
        
    def hacer_truco(self):
        if self.tipo == 'Humanoide':
            print(f'Soy {self.nombre} y estoy haciendo el paso del robot')
        else:
            print(f'Soy {self.nombre} por favor dame instrucciones')


#Instancia: que es un objeto específico creado a partir de la plantillas llamadas clases
robotin = Robot('Robotin', 'Humanoide')
tostadora = Robot('Tosty', 'Electrodomestico')

robotin.hacer_truco()
tostadora.hacer_truco()