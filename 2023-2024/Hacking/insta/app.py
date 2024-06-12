from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'super_secret_key'

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            token TEXT NOT NULL
        )
    ''')
    c.execute('''
        INSERT INTO users (username, password, token)
        VALUES ('bob', 'Mo2Pass', 'super_secret_token')
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = f"SELECT token FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return render_template('home.html', username=username, token=result[0])
    else:
        flash('Invalid credentials, please try again.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5002, debug=True)
