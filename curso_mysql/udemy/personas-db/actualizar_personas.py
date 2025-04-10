import mysql.connector   #incluir el modulo connector

peronas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user= "root",
    password="Adminmysql",
    database = "personas_db"
)

#ejecutar la sentencia UPDATE
cursor = peronas_db.cursor()
sentecia_sql = "UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id = %s"
valores = ("Victoria", "Flores", 45, 5)
cursor.execute(sentecia_sql, valores)
peronas_db.commit()
print("Se ha modificado la informacion")
cursor.close()
peronas_db.close()