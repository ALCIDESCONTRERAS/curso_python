#Clase Padre(Superclase)
class Personaje:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
        
    def presentarse(self):
        print(f'Hola soy {self.nombre} y mi poder es {self.poder}')
        
#Clase derivada(subclase)
class SuperHeroe(Personaje):
    def __init__(self, nombre, poder, ciudad):
        super().__init__(nombre, poder) #Utilizaremos super para pasarle la informacion a la super clase
        self.ciudad = ciudad
    
    def salvar_el_dia(self):
        print(f'{self.nombre} está salvando el día usando su poder {self.poder}')
    
    def salvar_la_ciudad(self):
        print(f'{self.nombre} está salvando la ciudad {self.ciudad} usando su poder {self.poder}')
        

class Villano(Personaje):
    def __init__(self, nombre, poder, archienemigo):
        super().__init__(nombre, poder)
        self.archienemigo = archienemigo
    
    def plan_maligno(self):
        print(f'!Cuidado¡ {self.nombre} está organinzando un plan malvado en contra de {self.archienemigo} usando su gran poder {self.poder}')
        
heroe = SuperHeroe('Capitán Código', 'Supermegarefactorización', 'Python city')
villano = Villano('Bugman', 'Crear errores en tus aplicaciones favoritas', 'Capitán código')

# heroe.presentarse()
# villano.presentarse()

heroe.salvar_la_ciudad()
villano.plan_maligno()