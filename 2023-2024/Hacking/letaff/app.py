from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Données fictives pour les utilisateurs et les courriels
users = {
    'bob.dilan@letaff.com': {'password': 'felix1995', 'name': 'Bob dilan'},
    'jane': {'password': 'smith', 'name': 'Jane Smith'}
}

mails = {
    'bob.dilan@letaff.com': [
        {'sender': 'Alice', 'subject': 'Confidentiel', 'date': 'June 10, 2024', 'content': 'Je vous apprend la fusion de notre groupe "Letaff" avec le groupe "LeTravail" , cette information doit rester confidentiel jusqu au jour J .'},
        {'sender': 'Bob', 'subject': 'Meeting', 'date': 'June 11, 2024', 'content': 'Meeting prevu le 12 juin.'}
    ],
    'jane': [
        {'sender': 'Carol', 'subject': 'Vacation', 'date': 'June 12, 2024', 'content': 'Nullam feugiat turpis vitae lorem.'},
        {'sender': 'David', 'subject': 'Project Update', 'date': 'June 13, 2024', 'content': 'Blandit eleifend.'}
    ]
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return redirect(url_for('mailbox', username=username))
        else:
            return render_template('login.html', error='Invalid username or password.')
    return render_template('login.html', error=None)

@app.route('/mailbox/<username>')
def mailbox(username):
    if username in users:
        user_mails = mails.get(username, [])
        user_info = users[username]
        return render_template('mailbox.html', username=username, user_info=user_info, mails=user_mails)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
