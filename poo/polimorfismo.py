class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        print("Hacer un sonido genérico")


class Guitarra(Instrumento):
    def __init__(self):
        super().__init__('La Guitarra')
    # Vamos a sobreescribir el método con un comportamiento propio de esta clase(OVERRIDE)
    def tocar(self):
        print(
            f"\033[91m{self.nombre} está haciendo el mejor solo de su vida usando bendings y ligados"
        )


class Bateria(Instrumento):
    def __init__(self, ):
        super().__init__('La Bateria')
    # Vamos a sobreescribir el método con un comportamiento propio de esta clase(OVERRIDE)
    def tocar(self):
        print(
            f"\033[92m{self.nombre} está llevando un gran ritmo en 4/4"
        )


class Piano(Instrumento):
    def __init__(self, ):
        super().__init__('El piano')
    # Vamos a sobreescribir el método con un comportamiento propio de esta clase(OVERRIDE)
    def tocar(self):
        print(
            f"\033[94m{self.nombre} nos está deleitando con un gran blues clásico"
        )

guitarra = Guitarra()
bateria = Bateria()
piano = Piano()

#Polimofismo es la capicidad de un método de hacer cosas dependiendo de la clase origen\033[91m
guitarra.tocar()
bateria.tocar()
piano.tocar()