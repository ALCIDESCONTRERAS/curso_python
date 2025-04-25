import tkinter as tk
from tkinter import ttk

#creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.resizable(0,0)
ventana.configure(background='#423d3c')

#Creamos una etiqueta(label) usar ttk para personzalizar
etiqueta = ttk.Label(ventana, text='Saludos')

#Cambiar el texto usando el metodo configure
etiqueta.configure(text='Nos vemos..')

#Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Caballo loco'

#Publicamos el componente
etiqueta.pack(pady=20)

#hacemos visible la ventana
ventana.mainloop()