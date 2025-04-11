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
#--------------------------------------------------------------------------------------------------------------
#CREAR TABLA
# sql = '''CREATE TABLE clientes(nombre VARCHAR(100), direccion VARCHAR(200))'''

#CREAR TABLA CON CLAVE PRIMARIA
# sql = '''CREATE TABLE empleados (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), puesto VARCHAR(100))'''

#AGREGAR CLAVE PRIMARIA A LA TABLA clientes
# sql = '''ALTER TABLE clientes ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'''
# cursor.execute(sql)

#VERIFICAR SI EXISTE LA TABLA O CONSULTAR LAS TABLAS QUE CONTIENE LA BASE DE DATOS
# cursor.execute('SHOW TABLES')

# for table in cursor:
#     print(table)

#--------------------------------------------------------------------------------------------------------------
#CREAR BASE DE DATOS
#cursor.execute('CREATE DATABASE computadoras')

#VERIFICAR si la base de dato existe
# cursor.execute('SHOW DATABASES')

# # #VER LO QUE CONTIENE CURSOR
# for bd in cursor:
#     print(bd)

#----------------------------------------------------------------------------------------------
#ENVIAR UN DATO A UNA TABLA
# sql = 'INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)'
# values = ('Maria', 'Barcelona. España')
# cursor.execute(sql, values)
#print(cursor.rowcount, 'registro insertado')

#ENVIAR VARIOS DATOS A UNA TABLA
# insertar_varios = 'INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)'
# values = [('Pedro', 'Madrid'),
#           ('Roberto', 'Valencia'),
#           ('Facundo', 'Valencia'),
#           ('Miguel', 'Asturias')]
# cursor.executemany(insertar_varios, values)
#print(cursor.rowcount, 'registro insertado')
#cursor.lastrowid para saber el último id que se ingresó

#------------------------------------------------------------------------------------------------
#traer toda la informacion
# seleccionar_info = 'SELECT * FROM clientes'
# cursor.execute(seleccionar_info)

#TRAER INFORMACION ESPECIFICA
# seleccionar_especifico = 'SELECT id, nombre FROM clientes'
# cursor.execute(seleccionar_especifico)

# clientes = cursor.fetchone()

# for cliente in clientes:
#     print(cliente)

#GUARDAR LOS CAMBIOS
#conection.commit()

#------------------------------------------------------------------------------------------------------
#TRAER INFORMACION ESPECIFICA CON FILTER
# sql = 'SELECT * FROM clientes WHERE nombre = "Pedro" '
# cursor.execute(sql)

#LIKE ES PARECIDO, CON EL PORCENTAJE DA IGUAL LO QUE HAY DESPUES
# sql = 'SELECT * FROM clientes WHERE nombre LIKE "M%"'
# cursor.execute(sql)

# %LETRA% ES PARA QUE DEVUELVA TODO LO QUE CONTENGA ESA LETRA O PALABRA
sql = 'SELECT * FROM clientes WHERE nombre LIKE "%e%"'
cursor.execute(sql)


clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)

conection.close()