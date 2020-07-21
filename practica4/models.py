from Apppop import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuario(db.Model):
    dni = db.Column(db.Integrer, primary_key=True)
    clave = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    pedido = db.relationship('Pedido', backref='usuario')

class Pedido(db.Model):
    numPedido = db.Column(db.Integrer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)
    cobrado = db.Column(db.Boolean, nullable=False)
    observacion = db.Column(db.Text)
    mesa = db.Column(db.Integrer, nullable=False)
    dnimozo = db.Column(db.Integrer, db.ForeignKey('usuario.dni'))
    item = db.relationship('Item', backref='pedido')

class Item(db.Model):
    numItem = db.Column(db.Integrer, primary_key=True)
    numPedido = db.Column(db.Integrer, db.ForeignKey('pedido.numPedido'))
    numProducto = db.Column(db.Integrer, db.ForeignKey('producto.numProducto'))
    precio = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(100), nullable=False)

class Producto(db.Model):
    numProducto = db.Column(db.Integrer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    preciounitario = db.Column(db.Float, nullable=False)
    item = db.relationship('Item', backref='producto')