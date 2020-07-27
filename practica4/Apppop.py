from flask import Flask,render_template, request, flash, redirect, url_for, session, escape
from passver import PasswordVer
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import ItemsPedidos, Pedidos, Productos, Usuarios


#Inicio
@app.route('/')
def index():
    titulo = "AppPop"
    if 'dni' in session and 'tipo' in session :
        return render_template('index.html', titulo=titulo, dni=escape(session['dni']), tipo=escape(session['tipo']))
    else:
        return render_template('index.html', titulo=titulo)
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
            
            flash('Verifica tus credenciales de acceso, DNI o contraseña inválidos')
            return redirect(url_for('login'))
        else:
            flash('Verifica tus credenciales de acceso, DNI o contraseña inválidos')
            return redirect(url_for('login'))
    else:
        return redirect(url_for("index"))
#Fin Login

#Log out
@app.route('/logout')
def logout():
    session.pop('dni')
    session.pop('tipo')

    return redirect(url_for('index'))

#Registrar Pedido
@app.route('/registrarpedido')
def registrarPedido():
    if "dni" in session and "tipo" in session:
        if escape(session['tipo']) == "Mozo":
            productos = Productos.query.all()
            titulo = "Registrar Pedido" 
            return render_template('registro_pedidos_mozo.html', titulo=titulo, productos=productos, dni=escape(session['dni']), tipo=escape(session['tipo']))
        elif escape(session['tipo']) == "Cocinero" :
            pass
        else :
            return redirect("logout")
    else:
        flash("Tip: Deberías Iniciar Sesión antes de realizar pedidos ;)")
        return redirect(url_for("login"))


@app.route('/registraredido', methods = ['POST'])
def handlePedido():
    if "dni" in session and "tipo" in session:
        if escape(session['tipo']) == "Mozo":
            if request.method == 'POST' :
                items_pedidos = request.form['items']
                items_pedidos = items_pedidos.split(',')
                nuevo_pedido = Pedidos(fecha= datetime.date.today(), total= float(request.form['total']), cobrado= False, observacion=request.form['observacion'], mesa=int(request.form['mesa']), dnimozo=int(escape(session['dni'])))
                db.session.add(nuevo_pedido)
                db.session.commit()
                for item in items_pedidos:
                    producto = Productos.query.filter_by( numProducto="{}".format(int(item))).first()
                    if producto is None:
                        flash('Error al cargar los items.')
                        return redirect(url_for('registrarPedido'))
                    else:
                        nuevo_item = ItemsPedidos(numPedido= nuevo_pedido.numPedido, numProducto= item, precio= producto.preciounitario, estado= 'Pendiente')
                        db.session.add(nuevo_item)
                db.session.commit()
                flash('Registro exitoso.')
                return redirect(url_for('registrarPedido'))
            else:
                flash('Algo no ha salido bien. Reintenta el pedido.')
                return redirect(url_for('registrarPedido'))
        elif escape(session['tipo']) == "Cocinero" :
            pass
        else :
            return redirect("logout")
    else:
        flash("Tip: Deberías Iniciar Sesión antes de realizar pedidos ;)")
        return redirect(url_for("login"))
#Fin Registrar Pedido

#Ver pedidos
@app.route('/pedidos')
def verPedidos():
    if "dni" in session and "tipo" in session:
        if escape(session['tipo']) == "Mozo":
            titulo = "Pedidos Vigentes" 
            pedidos = Pedidos.query.all()
            items = ItemsPedidos.query.all()
            productos = Productos.query.all()
            fecha = datetime.date.today()
            return render_template('listar_pedidos_mozo.html', titulo=titulo, pedidos=pedidos, productos = productos,items = items,fecha= fecha, dni=escape(session['dni']), tipo=escape(session['tipo']))
        elif escape(session['tipo']) == "Cocinero" :
            return redirect(url_for("index"))
        else :
            return redirect(url_for("logout"))


#Base de datos
@app.route('/prueba')
def prueba():
    usuarios = Usuarios.query.all()
    print(usuarios)
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
