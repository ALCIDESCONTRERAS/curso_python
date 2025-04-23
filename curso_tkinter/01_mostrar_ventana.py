import tkinter as tk

#creamos una ventana
ventana = tk.Tk()

#Redimensionamos la ventana
ventana.geometry('600x400')

#Modificar el titulo
ventana.title('Nueva ventana')

#Evitar redimensionar venta
ventana.resizable(0,0)

#Color de la ventana 
#Paleta de colores https://htmlcolorcodes.com/es/
ventana.configure(background='#423d3c')

#hacemos visible la ventana
ventana.mainloop()