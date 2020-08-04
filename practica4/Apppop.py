from flask import Flask,render_template, request, flash, redirect, url_for, session, escape
from passver import PasswordVer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import ItemsPedidos, Pedidos, Productos, Usuarios

#Before
@app.before_request
def before_request():
    if 'dni' in session and 'tipo' in session :
        pendientes = db.session.query(distinct(ItemsPedidos.numPedido)).join(Pedidos).filter(ItemsPedidos.estado=="Pendiente").count()
        session['pendientes'] = pendientes
#Fin Before

#Inicio
@app.route('/')
def index():
    titulo = "AppPop"
    if 'dni' in session and 'tipo' in session :
        return render_template('index.html', titulo=titulo, dni=escape(session['dni']), tipo=escape(session['tipo']), pendientes=escape(session['pendientes']))
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
    session.pop('pendientes')
    return redirect(url_for('index'))
#Fin Log out

#Registrar Pedido
@app.route('/registrarpedido')
def registrarPedido():
    if "dni" in session and "tipo" in session:
        if escape(session['tipo']) == "Mozo":
            productos = Productos.query.all()
            titulo = "Registrar Pedido" 
            return render_template('registro_pedidos_mozo.html', titulo=titulo, productos=productos, dni=escape(session['dni']), tipo=escape(session['tipo']), pendientes=escape(session['pendientes']))
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
        titulo = "Pedidos Vigentes" 
        if escape(session['tipo']) == "Mozo":
            fecha = datetime.date.today()
            pedidos = Pedidos.query.filter_by(fecha= fecha, cobrado= 0).all()
            return render_template('listar_pedidos_mozo.html', titulo=titulo, pedidos=pedidos, dni=escape(session['dni']), tipo=escape(session['tipo']), pendientes=escape(session['pendientes']))
        elif escape(session['tipo']) == "Cocinero" :
            #pedidos = Pedidos.query.all()
            pendientes = db.session.query(Pedidos).join(ItemsPedidos).filter(ItemsPedidos.estado=="Pendiente").all()
            fecha = datetime.date.today()            
            return render_template("listar_pedidos_cocinero.html", titulo=titulo, pedidos=pendientes, fecha= fecha, dni=escape(session['dni']), tipo=escape(session['tipo']), pendientes=escape(session['pendientes']))
        else :
            return redirect(url_for("logout"))
    else :
        return redirect(url_for("login"))

@app.route('/pedidos', methods = ['POST'])
def handleverPedidos():
    if "dni" in session and "tipo" in session:
        titulo = "Pedidos Vigentes" 
        if escape(session['tipo']) == "Mozo":
            return redirect(url_for("verPedidos"))
        elif escape(session['tipo']) == "Cocinero" :
            if request.method == 'POST' :
                items_pedidos = request.form.getlist('id-items')
                print(items_pedidos)
                for item in items_pedidos:
                    item_listo= ItemsPedidos.query.filter_by(numItem= item).first()
                    item_listo.estado = 'Listo'
                db.session.commit()
                flash('Cambio exitoso.')
                return redirect(url_for("verPedidos"))
        else :
            return redirect(url_for("logout"))
    else :
        return redirect(url_for("login"))

#Fin Ver pedidos

#Cobrar pedido
@app.route('/cobrarpedido/<int:pedido>')
def cobrarpedido(pedido):
    if "dni" in session and "tipo" in session:
        if escape(session['tipo']) == "Mozo":
            titulo = "Cobrar pedido"
            pedido_a_cobrar = Pedidos.query.filter_by(numPedido=pedido).first()
            if pedido_a_cobrar is None:
                flash('Error al cargar el pedido.')
                return redirect(url_for('verPedidos'))
            else:
                return render_template('cobrar_pedido.html', titulo=titulo, pedido=pedido_a_cobrar, dni=escape(session['dni']), tipo=escape(session['tipo']), pendientes=escape(session['pendientes']))
        elif escape(session['tipo']) == "Cocinero" :
            return redirect(url_for("index"))
        else :
            return redirect(url_for("logout"))
    else :
        return redirect(url_for("login"))

@app.route('/cobrarpedido/<int:pedido>', methods = ['POST'])
def handlecobrarpedido(pedido):
    if "dni" in session and "tipo" in session:
        if escape(session['tipo']) == "Mozo":
            if request.method == 'POST' :
                pedido_a_cobrar = Pedidos.query.filter_by(numPedido=pedido).first()
                pedido_a_cobrar.cobrado = True
                db.session.commit()
                flash('Cobro exitoso.')
                return redirect(url_for("verPedidos"))
        elif escape(session['tipo']) == "Cocinero" :
            pass
        else :
            return redirect("logout")
    else:
        return redirect(url_for("login"))
#Fin Cobrar Pedido

if __name__ == '__main__':
    app.run(debug=True)
