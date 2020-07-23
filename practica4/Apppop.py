from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    titulo = "AppPop" 
    return render_template('index.html', titulo=titulo)

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

# @app.route('/registrarpedido')
# def registrarPedido():
#     titulo = "AppPop Registrar Pedido" 
#     return render_template('registroP.html', titulo=titulo)

if __name__ == '__main__':
    app.run(debug=True)