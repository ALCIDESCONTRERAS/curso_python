import mysql.connector   #incluir el modulo connector

peronas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user= "root",
    password="Adminmysql",
    database = "personas_db"
)

#ejecutar la sentencia SELECT
cursor = peronas_db.cursor()
cursor.execute("SELECT * FROM personas");
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)
    
cursor.close()
peronas_db.close()