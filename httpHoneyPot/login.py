from flask import Flask, render_template, request, redirect, session, url_for, flash
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

valid_username = "user"
valid_password = "password"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    current_time = time.time()

    if 'last_request_time' in session:
        time_diff = current_time - session['last_request_time']

        # If the user is too fast, treat it as a bot and redirect
        if time_diff < 5:
            flash("Failed to authenticate. Redirecting to the security page...", "error")
            return redirect("http://localhost:5001/fake-login")

    session['last_request_time'] = current_time

    username = request.form['username']
    password = request.form['password']

    if username == valid_username and password == valid_password:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash("Failed to authenticate. Please try again.", "error")
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
