print("****** abrir un archivo en modo exclusivo ******")

nombre_archivo = "mi_archivo.txt"
try:
    #abrimos el archivo modo exclusivo (x), no se puede volver a crear el archivo
    with open(nombre_archivo, "x") as archivo:
        archivo.write("escritura modo exclusivo\n")   
        archivo.write("ver si es util\n")
    print(f"se ha creado el archivo {nombre_archivo}")
except FileExistsError as e:
    print(f"el archivo {nombre_archivo} ya existe")
    print(f"Detalle del error: {e}")