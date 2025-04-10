print("*********leer archivo con python***********")

nombre_archivo = "mi_archivo.txt"

#Leer un archivo usando el metodo readlines
with open(nombre_archivo, "r") as archivo:
    #leer todas las lineas del archivo
    #print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())
        

print("-------------------------------------------------------------------")
#leer el contenido del archivo usando read
#mejor forma para no iterar
print("leyendo el archivo con el metodo read")
with open(nombre_archivo, "r") as archivo:
    print(archivo.read().strip())