from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuarios(db.Model):
    dni = db.Column(db.Integer, primary_key=True)
    clave = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)

class Pedidos(db.Model):
    numPedido = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)
    cobrado = db.Column(db.Boolean, nullable=False)
    observacion = db.Column(db.Text)
    mesa = db.Column(db.Integer, nullable=False)
    dnimozo = db.Column(db.Integer, db.ForeignKey('Usuarios.DNI'))

class ItemsPedidos(db.Model):
    numItem = db.Column(db.Integer, primary_key=True)
    numPedido = db.Column(db.Integer, db.ForeignKey('Pedidos.NumPedido'))
    numProducto = db.Column(db.Integer, db.ForeignKey('Productos.NumProducto'))
    precio = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(100), nullable=False)

class Productos(db.Model):
    numProducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    preciounitario = db.Column(db.Float, nullable=False)