class CajaFuerte:
    def __init__(self, clave, cantidad):
        self.__clave = clave
        self.__cantidad = cantidad
    
    
    #Getters: son métodos para poder obtener información de un atributo privado    
    # def obtener_clave(self):
    #     return self.__clave
    
    def verificar_clave(self, clave):
        return self.__clave == clave
    
    
    def obtener_cantidad(self, clave):
        if self.verificar_clave(clave):
            return self.__cantidad
        else:
            print('la clave que colocaste es incorrecta')
    
    #Setters: son métodos para estableces nuevos valores a los atributos privados
    def establecer_clave(self, clave_nueva, clave):
        if self.verificar_clave(clave):
            if len(clave_nueva) < 4:
                print('La clave debe tener al menos 4 catactares')
            else:
                print('la clave fue cambiada con éxito')
                self.__clave = clave_nueva
        else:
            print('la clave que colocaste es incorrecta')
    
    def establecer_cantidad(self, cantidad_nueva, clave):
        if self.verificar_clave(clave):
            if cantidad_nueva <= 0:
                print('No se puede agregar un valor en cero')
            else:
                print('la cantidad fue cambiada con éxito')
                self.__cantidad = cantidad_nueva
        else:
            print('la clave que colocaste es incorrecta')
    

caja = CajaFuerte('1234', 1000)


caja.establecer_clave('4567', '1234')

caja.establecer_cantidad(4500, '4567')


