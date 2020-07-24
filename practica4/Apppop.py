from flask import Flask,render_template, request, flash, redirect, url_for, session, escape
from passver import PasswordVer
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import ItemsPedidos, Pedidos, Productos, Usuarios


#Inicio
@app.route('/')
def index():
    titulo = "AppPop" 
    return render_template('index.html', titulo=titulo, dni=escape(session['dni']), tipo=escape(session['tipo']))
#Fin Inicio

#Login
@app.route('/login')
def login():
    titulo = "AppPop Login" 
    if 'dni' in session :
        return redirect(url_for('index'))
    else:
        return render_template('login.html', titulo=titulo)

@app.route('/login', methods = ['POST'])
def handledata():
    titulo = "AppPop Login" 
    if request.method == 'POST' :
        if(request.form['dni'] and request.form['password']):
            usuario = Usuarios.query.filter_by(dni=request.form['dni']).first()
            if(type(usuario) is not None):
                passver = PasswordVer(request.form['password'])
                if(passver.validarPassword(usuario.clave)):
                    session["dni"] = usuario.dni
                    session["tipo"] = usuario.tipo
                    return redirect(url_for('index'))
            
            flash('Verifica tus credenciales de acceso, DNI o contrasenia invalidos')
            return redirect(url_for('login'))
        else:
            flash('Verifica tus credenciales de acceso, DNI o contrasenia invalidos')
            return redirect(url_for('login'))
#Fin Login

#Log out
@app.route('/logout')
def logout():
    session.pop('dni')
    session.pop('tipo')

    return redirect(url_for('index'))

#Registrar Pedido
@app.route('/registrarpedido', methods = ['POST'])
def registrarPedido():
    productos = Productos.query.all()
    titulo = "Registrar Pedido" 
    return render_template('registro_pedidos_mozo.html', titulo=titulo, productos=productos)
#Fin Registrar Pedido

#Base de datos
@app.route('/prueba')
def prueba():
    usuarios = Usuarios.query.all()
    print(usuarios)
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
