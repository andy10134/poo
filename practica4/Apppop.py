from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import Pedido, Usuario, Item, Producto

@app.route('/')
def index():
    titulo = "AppPop" 
    return render_template('index.html', titulo=titulo)

@app.route('/login')
def login():
    titulo = "AppPop Login" 
    return render_template('login.html', titulo=titulo)


if __name__ == '__main__':
    app.run(debug=True)