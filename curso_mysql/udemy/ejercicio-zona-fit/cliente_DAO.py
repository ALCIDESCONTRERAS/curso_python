from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    INSERTAR = "INSERT INTO cliente(nombre,apellido,membresia) VALUES(%s, %s, %s)"
    ACTUALIZAR = " UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id = %s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"
    
    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod            
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount            
        except Exception as e:
            print(f'Ocurrió un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
        
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'ocurrió un error al actualizar un cliente: {e}')            
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valor_id = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valor_id)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al eliminar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
                
if __name__ == '__main__':
    #insertar cliente
    # cliente1 = Cliente(nombre='Pedro', apellido='Perez', membresia=50)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'clientes insertados: {clientes_insertados}') 
      
    #actualizar un cliente
    # cliente1 = Cliente(id=3, nombre="Juana", apellido='Platón', membresia='60')
    # cliente_actualizado= ClienteDAO.actualizar(cliente1)
    # print(f'Clientes actualizados: {cliente_actualizado}')
    
    #eliminar cliente
    cliente1 = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente1)
    print(f'clientes eliminados: {clientes_eliminados}')
    #Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

                
                
        
    
    