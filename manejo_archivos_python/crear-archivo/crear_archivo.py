#creamos el archivo
nombre_archivo = "mi archivo.txt"

#Mejor forma de abrir archivos

#buena practica python
#aqui se abre el archivo y se cierra automaticamente, lo renombramos con (as)
with open(nombre_archivo, "w") as archivo:
    archivo.write("Hola como estas\n")
    archivo.write("estoy agregando informacion al archivo\n")

# Esto mas complicado

# #abrimos el archivo
# archivo = open(nombre_archivo, "w")

# #escribimos en el archivo
# archivo.write("Hola como estas\n")
# archivo.write("estoy agregando informacion al archivo\n")

# #se cierra el archivo
# archivo.close()


print(f"Se creó el archivo: {nombre_archivo}")