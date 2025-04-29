from mysql.connector import Error, pooling

class Conexion:
    pool = None
    
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
               cls.pool = pooling.MySQLConnectionPool(
                   pool_name='almacen',
                   pool_size= 5,
                   host = 'localhost',
                   port = '3306',
                   database = 'almacendb',
                   user = 'root',
                   password = 'Adminmysql'
               )
               return cls.pool
            except Error as e:
                print(f'Ocurrió un error al obtener conexión: {e}')
    
        else:
            return cls.pool	
     
    @classmethod    
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls, conexion):
        return conexion.close()
    

    
    
    