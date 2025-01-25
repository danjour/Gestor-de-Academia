from flask import Flask, render_template, request, redirect,url_for
import sqlite3
from threading import local
from datetime import datetime
import hashlib

app = Flask(__name__)

thread_local = local()

def get_connection():
    """
    Retrieve a SQLite connection for the current thread.
    Ensures each thread gets its own connection.
    """
    if not hasattr(thread_local, "connection"):
        thread_local.connection = sqlite3.connect(r"C:\Users\eduar\Documents\GitHub\Gestor-de-Academia\remina.db", check_same_thread=False)
        thread_local.connection.row_factory = sqlite3.Row 
    return thread_local.connection

def generate_hash(value):
    hash_object = hashlib.sha256(value.encode())
    return hash_object.hexdigest()


@app.route('/')
def index():
    return render_template('home/home.html')

#Generic route for login page
@app.route('/login')
def login():
    return render_template('clients/login.html')

#Generic route for register a new client
@app.route('/new_client/<plan>')
def new_client(plan):
    return render_template('manager/register.html', plan=plan)

@app.route('/payment', methods=['GET', 'POST'])
def addclient_payment():
    if request.method == 'POST':
        data = request.form 

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        gender = data.get('gender')
        gender_other = data.get('gender-other', '')  # Default to empty if not provided
        address = data.get('address')
        house = data.get('house')
        neighborhood = data.get('neighborhood')
        city = data.get('city')
        birthdate = data.get('birthdate')
        cpf = data.get('cpf')
        payment_method = data.get('payment_method', '')
        plan = data.get('plan', '')
        plan_value = float(data.get('plan_value', 0.0))
        
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO clients (
                    name, email, phone, gender, gender_other, address, house, neighborhood, city, 
                    birthdate, age, cpf, payment_method, plan, plan_value, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, DATE('now'))
            """
            cursor.execute(query, (name, email, phone, gender, gender_other, address, house, 
                                   neighborhood, city, birthdate, age, cpf, payment_method, plan, plan_value))
            conn.commit()
            
            client_id = cursor.lastrowid
            
            client_hash = generate_hash(str(client_id))

            cursor.execute("UPDATE clients SET client_hash = ? WHERE id = ?", (client_hash, client_id))
            
            conn.commit()

            return redirect(url_for('payment_page',id=client_hash))
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return render_template('manager/register.html', success=False, error=str(e))
    else:
        return "Invalid Request Method", 405
    
    
@app.route('/payment_page')
def payment_page():
    client_hash = request.args.get('id')
    print(f"Client Hash: {client_hash}")
    return render_template('clients/payment.html',client_hash=client_hash)


@app.route('/finish_payment', methods=['GET', 'POST'])
def finish_payment():
    if request.method == 'POST':
        data = request.form  # Access form data
        print(f"Form Data: {data}")
        client_hash = data.get('client_hash')

        
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query_plan = """
                UPDATE clients 
                SET payment_method = ?, recurrence = ?, plan_value = ?
                WHERE client_hash = ?
            """
            
            query = """
                INSERT INTO clients_plans_recurrence (
                    client_hash,recurrence,plan,plan_value,d_date_start,d_date_end
                )
                VALUES (?, ?, ?, ?, DATE('now'),DATE('now', '+1 month'))
            """
            
            cursor.execute(query, (client_hash, "monthly", "plan1", 99.99,))
            cursor.execute(query_plan, ("debit", "monthly", 99.99, client_hash))

            conn.commit()

            return redirect(url_for('payment_page',_=client_hash))
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return render_template('manager/register.html', success=False, error=str(e))

    else:
        return "Invalid Request Method", 405





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