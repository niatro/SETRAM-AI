from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mabel10'
#Ignacio trabajara un poquito aqui
# This would be replaced with a real database
users = {'user1': '1234'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials'
    else:
        return '''
            <form method="post">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        '''

@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    else:
        return 'You are not logged in'

if __name__ == '__main__':
    app.run(debug=True)