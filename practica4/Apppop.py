from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "AppPop" 
    return render_template('index.html', titulo=titulo)

@app.route('/login')
def login():
    titulo = "Login" 
    return render_template('login.html', titulo=titulo)


if __name__ == '__main__':
    app.run(debug=True)