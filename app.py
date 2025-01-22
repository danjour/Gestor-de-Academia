from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home/home.html')


#Generic route for login page
@app.route('/login')
def login():
    return render_template('clients/login.html')

#Generic route for register a new client
@app.route('/new_client')
def new_client():
    return render_template('manager/register.html')

#For a while, it will be simple, but in the next step, it will become more complex as we put the database in a secure place.
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        pass
        return redirect('/login')  

    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)