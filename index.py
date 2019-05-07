from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

@app.route('/')
def first_pg():
    return render_template('index.html')
@app.route('/login')
def login_pg():
    return render_template('login_page.html')
if __name__ == '__main__':
    app.run(debug=True)