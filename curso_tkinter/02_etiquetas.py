import tkinter as tk

#creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.resizable(0,0)
ventana.configure(background='#423d3c')


#Creamos una etiqueta(label)
etiqueta = tk.Label(ventana, text='Saludos')

#hacemos visible la ventana
ventana.mainloop()