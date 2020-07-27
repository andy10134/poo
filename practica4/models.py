from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__= 'usuarios'
    dni = db.Column(db.Integer, primary_key=True, nullable=False)
    clave = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    pedidos = relationship("Pedidos", backref='usuarios', cascade="all, delete-orphan", lazy='dynamic')

class Pedidos(db.Model):
    __tablename__= 'pedidos'
    numPedido = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    total = db.Column(db.Float, nullable=False)
    cobrado = db.Column(db.Boolean, nullable=False)
    observacion = db.Column(db.Text)
    mesa = db.Column(db.Integer, nullable=False)
    dnimozo = db.Column(db.Integer, db.ForeignKey('usuarios.dni'))
    items = relationship("ItemsPedidos", backref='pedidos', cascade="all, delete-orphan", lazy='dynamic')

class ItemsPedidos(db.Model):
    __tablename__= 'ItemsPedidos'
    numItem = db.Column(db.Integer, primary_key=True)
    numPedido = db.Column(db.Integer, db.ForeignKey('pedidos.numPedido'))
    numProducto = db.Column(db.Integer, db.ForeignKey('productos.numProducto'))
    precio = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    producto = relationship("Productos", backref='itemspedidos')

class Productos(db.Model):
    __tablename__= 'productos'
    numProducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    preciounitario = db.Column(db.Float, nullable=False)