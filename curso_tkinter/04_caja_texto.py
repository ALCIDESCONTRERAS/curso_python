import tkinter as tk
from tkinter import ttk

#creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.resizable(0,0)
ventana.configure(background='#423d3c')

def mostrar():
    texto = caja_texto.get() #Recuperamos el valor de la caja de texto
    print(f'Texto proporcionado: {texto}')
    etiqueta['text'] = texto

#Caja de texto
caja_texto = ttk.Entry(ventana, font=('Arial', 15))
caja_texto.pack(pady=20)

#Agregar un boton
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=20)

#Agregamos etiqueta
etiqueta = ttk.Label(ventana, text='Valor inicial')
etiqueta.pack(pady=20)

#hacemos visible la ventana
ventana.mainloop()