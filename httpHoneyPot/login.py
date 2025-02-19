"""
login.py
========

This module defines the Flask application for user authentication.
It provides the following routes:

- `/` : Renders the login form.
- `/dashboard` : Shows the user dashboard after a successful login.
- `/login` : Processes login requests, implementing a honeypot mechanism to
  detect rapid login attempts (bot behavior).
- `/logout` : Logs out the user and clears the session.

Note:
    When login requests are made too rapidly (less than 5 seconds apart),
    the application (unless in testing mode) redirects to a honeypot page at
    "http://localhost:5003/fake-login".
"""

from flask import Flask, render_template, request, redirect, session, url_for, flash
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

valid_username = "user"
valid_password = "password"

@app.route('/')
def home():
    """
    Home page route.
    
    Renders the login form.
    """
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Dashboard route.
    
    If the user is authenticated (i.e. 'username' in session), renders the dashboard.
    Otherwise, redirects to the login form.
    """
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    """
    Login route.
    
    Processes login attempts:
    
    - Checks for rapid repeated attempts; if detected (and not in testing mode),
      redirects to the honeypot page.
    - On valid credentials, sets the session and redirects to the dashboard.
    - On failure, flashes an error message and redirects back to the login form.
    """
    current_time = time.time()

    if not app.testing and 'last_request_time' in session:
        time_diff = current_time - session['last_request_time']
        if time_diff < 5:
            flash("Failed to authenticate. Redirecting to the security page...", "error")
            return redirect("http://localhost:5003/fake-login")

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
    """
    Logout route.
    
    Clears the user session, flashes a logout message, and redirects the user back
    to the login page.
    """
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
