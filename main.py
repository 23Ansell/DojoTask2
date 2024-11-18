from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash # CHATGPT - Responsible for hashing passwords
from pocketbase import PocketBase
import sqlite3
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

def is_logged_in():
    return 'user_id' in session

def get_db_connection():
    conn = sqlite3.connect('db.db')
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(conn):
    conn.close()

def init_db(): #CHATGPT - Responsible for initializing the database
    with app.app_context():
        conn = get_db_connection()
        with app.open_resource('database.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        print("done")
        close_db_connection(conn)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Email already registered. Please use a different email or log in.', 'danger')
            close_db_connection(conn)
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        cursor.execute('INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)',
                       (full_name, email, hashed_password))
        conn.commit()
        close_db_connection(conn)

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html', is_logged_in=is_logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        close_db_connection(conn)

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['full_name'] = user['full_name']
            flash('You are now logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', is_logged_in=is_logged_in)

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', is_logged_in=is_logged_in)

@app.route('/about')
def about():
    return render_template('about.html', is_logged_in=is_logged_in)

@app.route('/booking')
def booking():
    return render_template('booking.html', is_logged_in=is_logged_in)

@app.route('/instructors')
def instructors():
    return render_template('instructors.html', is_logged_in=is_logged_in)

@app.route('/courses')
def courses():
    return render_template('courses.html', is_logged_in=is_logged_in)

@app.route('/account')
def account():
    return render_template('account.html', is_logged_in=is_logged_in)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)