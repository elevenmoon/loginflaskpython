from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb
from flask_session import Session

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'sql.freedb.tech'
app.config['MYSQL_USER'] = 'freedb_cvgomez17'
app.config['MYSQL_PASSWORD'] = '@EY%Qh8Ym3W$R$7'
app.config['MYSQL_DB'] = 'freedb_condipastel'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

#funcion de login
@app.route('/acceso-login', methods=["GET","POST"])
def login():

    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        print(_correo)
        _password = request.form['txtPassword']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user=%s AND password=%s", (_correo, _password,))
        account = cur.fetchone()
        print(account)

        if account:
            session['logueado'] = True
            session['id'] = account['id']
            session['nombre'] = account['user']
            print(session)
            return render_template('admin.html')
        else:
            msg = 'Invalid credentials. Please try again.'
            return render_template('index.html', mensaje='usuario incorrecto')

if __name__ ==  '__main__':
    app.secret_key = 'romanlugo super secret key'
    app.config["SESSION_PERMANENT"] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, host='0.0.0.0', port=3306, threaded=True)

Session(app)