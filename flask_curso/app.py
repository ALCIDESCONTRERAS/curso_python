from flask import Flask, render_template, redirect, url_for
from cliente_DAO import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

app = Flask(__name__)
app.config['SECRET_KEY'] = 'llave_secreta_123'

titulo_app = 'Zona Fit (GYM)'

@app.route('/')
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos en el path de inicio')
    #Recuperamos los datos de la bd
    clientes_db = ClienteDAO.seleccionar()
    #Creamos un objeto de cliente vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    #Crear cliente vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    if cliente_forma.validate_on_submit():
        #Llenamos el obj cliente con los datos del formulario
        cliente_forma.populate_obj(cliente)
        if not cliente.id:
            #Guardamos el nuevo cliente en la bd
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)        
    #Redireccionar a la pagina de inicio
    return redirect(url_for('inicio'))
    
@app.route('/limpiar')        
def limpiar():
    return redirect(url_for('inicio'))
        
@app.route('/editar/<int:id>')        
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    #Recuperar el listado de clientes para volver a mostrarlo
    cliente_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, forma=cliente_forma, clientes=cliente_db)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    ClienteDAO.eliminar(cliente)  
    return redirect(url_for('inicio'))






if __name__ == '__main__':
    app.run(debug=True)