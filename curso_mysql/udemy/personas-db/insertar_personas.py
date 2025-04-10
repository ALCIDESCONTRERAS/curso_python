import mysql.connector   #incluir el modulo connector

peronas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user= "root",
    password="Adminmysql",
    database = "personas_db"
)

#insertar registros desde python a mysql (INSERT)

cursor = peronas_db.cursor()
sentencias_sql = "INSERT INTO personas (nombre, apellido, edad) VALUES(%s, %s, %s)"
valores = ("Victor", "Ramos", 46)
cursor.execute(sentencias_sql, valores)
peronas_db.commit() #guardar en la base de datos
print(f"se ha agregado en la base de datos {valores}")
cursor.close()
peronas_db.close()