print("-----------anexar informacion a nuestro archivo------------")

nombre_archivo = "mi_archivo.txt"

#anexar informacion (a) append
with open(nombre_archivo, "a") as archivo:
    #Anexar informacion al archivo
    archivo.write("Anexando informacion\n")
    archivo.write("Saliendo de anexar informacion..\n")

print(f"Se ha anexado informacion al archivo {nombre_archivo}")