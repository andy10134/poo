from models import db, Usuarios, ItemsPedidos, Pedidos, Productos
from flask_sqlalchemy import SQLAlchemy

class Conexion():

    __db = None

    def __init__(self, aplicacion):
        self.__db = SQLAlchemy(aplicacion)
    
    def validarDNI(self):
        return Usuarios.query.all()
