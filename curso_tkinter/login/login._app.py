import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
#Grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

#Creamos estilos para la aplicacion
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white', fieldbackground='black')
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active', '#0a9396')])


#Agregar un frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

#Agregar etiqueta
usuario = ttk.Label(ventana, text='Usuario:')


#titulo
titulo = ttk.Label(frame, text='Login', font=('Arial', 20))
titulo.grid(row=0, column=0, columnspan=2)

#Agregar etiqueta e input de usuario 
usuario_etiqueta = ttk.Label(frame, text='Usuario:')
usuario_input = ttk.Entry(frame)
password_etiqueta = ttk.Label(frame, text='Password:')
password_input = ttk.Entry(frame, show='*')

usuario_etiqueta.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
usuario_input.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
password_etiqueta.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
password_input.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

#Boton login
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event):
    usuario = usuario_input.get()
    password = password_input.get()
    #Si usuario = root y password = admin son valores correctos
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login', message='Datos correctos')
    else:
        showerror(title='Login', message='Datos incorrectos')
   
#asociar eventos al boton de login
login_boton.bind('<Return>', validar) # presionar la tecla enter
login_boton.bind('<Button-1>', validar) # peresionar click izquierdo


#publicar
frame.grid(row=0, column=0)





ventana.mainloop()

