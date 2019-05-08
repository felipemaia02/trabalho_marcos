from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pcgo2013'
app.config['MYSQL_DATABASE_DB'] = 'contatos'

@app.route('/')
def first_pg():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_pg():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        cursor = mysql.get_db().cursor()

        idlogin = get_idlogin(cursor, login, senha)

        if idlogin == None:
            return render_template('login_page.html', erro = 'Login/senha incorretos!')

        else:
            cursor.mysql.get_db().cursor()
            return render_template('')


if __name__ == '__main__':
    app.run(debug=True)