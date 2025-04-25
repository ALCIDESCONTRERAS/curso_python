import tkinter as tk
from tkinter import ttk

#creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.resizable(0,0)
ventana.configure(background='#423d3c')


#command en boton
def saludar(nombre):
    print(f'saludos {nombre}')

#Botones
boton1 = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Caballo'))
boton1.pack(pady=20)

#hacemos visible la ventana
ventana.mainloop()