from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import ItemsPedidos, Pedidos, Productos, Usuarios


#Inicio
@app.route('/')
def index():
    titulo = "AppPop" 
    return render_template('index.html', titulo=titulo)
#Fin Inicio

#Login
@app.route('/login')
def login():
    titulo = "AppPop Login" 
    return render_template('login.html', titulo=titulo)

@app.route('/login', methods = ['POST'])
def handledata():
    titulo = "AppPop Login" 
    if request.method == 'POST' :
        if(request.form['dni'] and request.form['password']):
            dni = request.form['dni']
            password = request.form['password']

            return render_template('index.html', titulo=titulo)    
        else:
            return render_template('login.html', titulo=titulo)
#Fin Login

#Registrar Pedido
@app.route('/registrarpedido')
def registrarPedido():
    titulo = "Registrar Pedido" 
    return render_template('registroP.html', titulo=titulo)
#Fin Registrar Pedido

#Base de datos
@app.route('/prueba')
def prueba():
    usuarios = Usuarios.query.all()
    print(usuarios)
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
