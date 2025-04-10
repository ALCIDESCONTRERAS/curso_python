import mysql.connector

conection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Adminmysql',
    port = '3306',
    database = 'computadoras'
)

#print(conection)

#CREAR CURSOR
# En MySQL, un cursor es una estructura que permite recorrer fila por fila los resultados de una consulta,
# dentro de procedimientos almacenados. Es útil cuando necesitas realizar operaciones por cada fila de un 
# conjunto de resultados, algo que no se puede hacer directamente con una sola sentencia SQL.

# ¿Cuándo se usa un cursor?
# Se usa cuando:

# Necesitas procesar datos fila por fila.

# No puedes hacer lo que necesitas con un simple UPDATE, DELETE o SELECT con condiciones.

# Estás dentro de un procedimiento almacenado y necesitas control más granular sobre los datos.
cursor = conection.cursor()

#VERIFICAR SI EXISTE LA TABLA
cursor.execute('SHOW TABLES')

for table in cursor:
    print(table)

#CREAR TABLA
# sql = '''CREATE TABLE clientes(nombre VARCHAR(100), direccion VARCHAR(200))'''

#CREAR TABLA CON CLAVE PRIMARIA
sql = '''CREATE TABLE empleados (id INT AUTO_INCREMENT PRIMARY_KEY, nombre VARCHAR(255), puesto VARCHAR(100))'''
cursor.execute(sql)

#CREAR BASE DE DATOS
#cursor.execute('CREATE DATABASE computadoras')

#VERIFICAR si la base de dato existe
# cursor.execute('SHOW DATABASES')

# # #VER LO QUE CONTIENE CURSOR
# for bd in cursor:
#     print(bd)

#GUARDAR LOS CAMBIOS
conection.commit()

conection.close()