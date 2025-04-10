from cliente_DAO import ClienteDAO
from cliente import Cliente

print('*** Clientes Zona Fit (GYM) ***')

opcion = None
while opcion != 5:
    print('''
          1. Listar clientes
          2. Agregar cliente
          3. Modificar cliente
          4. Eliminar cliente
          5. Salir''')
    opcion = int(input('Escribe tu opción (1-5): '))
    try:
        if opcion == 1:
            clientes = ClienteDAO.seleccionar()
            for cliente in clientes:
                print(cliente)
        elif opcion == 2:
            nombre = input('Agrega el Nombre: ')
            apellido = input('Agrega el Apellido: ')
            membresia = int(input('Agrega la membresia: '))
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            print('Cliente Agregado!!')
        elif opcion == 3:
            id= int(input('agrega el id del cliente: '))
            nombre = input('Agrega el Nombre: ')
            apellido = input('Agrega el Apellido: ')
            membresia = int(input('Agrega la membresia: '))
            cliente = Cliente(id, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            print('Cliente actualizado correctamente')
        elif opcion == 4:
            id = int(input('Indica el id del cliente que quieres eliminar: '))
            cliente = Cliente(id=id)
            ClienteDAO.eliminar(cliente)
            print('cliente eliminado correctamente!!!')
        else:
            opcion == 5
            print('saliste de la aplicación')
    except Exception as e:
        print(f'Ocurrió un error: {e}')