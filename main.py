from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash # CHATGPT - Responsible for hashing passwords
import sqlite3
import uuid
import os
import ssl
from datetime import datetime

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

def is_logged_in():
    return 'user_id' in session

def is_admin():
    if is_logged_in():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
        user = cursor.fetchone()
        conn.close()
        return user['is_admin']
    else:
        pass

def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'pb_data', 'data.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

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
            conn.close()
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        cursor.execute('INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)',
                       (full_name, email, hashed_password))
        conn.commit()
        conn.close()

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['full_name'] = user['full_name']
            flash('You are now logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/about')
def about():
    return render_template('about.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/booking')
def booking():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM events')
    events = cursor.fetchall()
    conn.close()

    e = []
    for event in events:
        event_dict = dict(event)
        event_dict['date'] = datetime.strptime(event['date'], "%Y-%m-%d %H:%M:%S.000Z").strftime("%d/%m/%Y %H:%M")
        e.append(event_dict)

    return render_template('booking.html', is_logged_in=is_logged_in, is_admin=is_admin, events=e)

@app.route('/book', methods=['POST'])
def book():
    if not is_logged_in():
        flash('Please log in to book the event', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        event_id = request.form['event_id']
        user_id = session['user_id']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bookings (event_id, user_id, registration_date, status) VALUES (?, ?, ?, ?)',
                       (event_id, user_id, datetime.now(), 'pending'))
        cursor.execute('UPDATE events SET participants = participants + 1 WHERE id = ?', (event_id,))
        conn.commit()
        conn.close()
        flash('You have successfully booked the event', 'success')
        return redirect(url_for('booking'))
    
@app.route('/waiting_list', methods=['POST'])
def waiting_list():
    if not is_logged_in():
        flash('Please log in to join the waiting list', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        event_id = request.form['event_id']
        user_id = session['user_id']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO waiting_list (event_id, user_id, registration_date, status) VALUES (?, ?, ?, ?)',
                       (event_id, user_id, datetime.now(), 'waiting'))
        conn.commit()
        conn.close()
        flash('You have successfully joined the waiting list', 'success')
        return redirect(url_for('booking'))

@app.route('/courses')
def courses():
    return render_template('courses.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/account')
def account():
    return render_template('account.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/adminpanel')
def adminpanel():
    return render_template('adminpanel.html', is_logged_in=is_logged_in, is_admin=is_admin)

@app.route('/forgotpassword')
def forgot_password():
    flash('That sucks!!!', 'danger')
    return redirect (url_for('login'))

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certs/fullchain.pem', 'certs/privkey.pem')
    app.run(host='0.0.0.0', port=5141, debug=True, ssl_context=context)