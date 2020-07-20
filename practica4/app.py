from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def bienvenida():
    return render_template('inicio.html')

@app.route('/mensaje/saludo')
def saludo():
    return 'Hola internauta esta es mi primer aplicación con Flask!'
  
if __name__ == '__main__':
    app.run(debug=True)