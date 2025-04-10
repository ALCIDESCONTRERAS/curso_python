import mysql.connector   #incluir el modulo connector

peronas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user= "root",
    password="Adminmysql",
    database = "personas_db"
)

#ejecutar la sentencia DELETE
cursor = peronas_db.cursor()
snetencia_sql = "DELETE FROM personas WHERE id=%s"
valores = (5,)
cursor.execute(snetencia_sql, valores)
peronas_db.commit()
print("Se eliminó correctamente la persona")

cursor.close()
peronas_db.close()