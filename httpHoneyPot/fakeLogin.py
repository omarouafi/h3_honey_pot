"""
fakeLogin.py
============

This module defines a Flask application that acts as a honeypot for capturing
malicious login attempts. It simulates a login page that logs details about
attempted logins (e.g., IP address, attempted username, and password) to a file
named 'honeypot_logs.txt'. Additionally, if requests come in too rapidly (within
10 seconds), it logs a message about suspicious behavior.
"""

import logging
import time
from flask import Flask, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

logging.basicConfig(
    filename="honeypot_logs.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@app.route('/fake-login', methods=['GET', 'POST'])
def fake_login():
    """
    Fake Login route (honeypot).
    
    - On GET requests, renders the fake login page.
    - On POST requests, logs the attacker's IP, username, and password,
      flashes an error message, and renders the fake login page.
    
    Also logs suspicious behavior if requests occur too rapidly (within 10 seconds).
    """
    current_time = time.time()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))

    if 'last_fake_request_time' in session:
        time_diff = current_time - session['last_fake_request_time']
        if time_diff < 10:
            ip = request.remote_addr
            logging.info(f"[{formatted_time}] Suspicious behavior detected. IP: {ip} made requests within {time_diff:.2f} seconds")
    
    session['last_fake_request_time'] = current_time

    if request.method == 'POST':
        ip = request.remote_addr
        username = request.form['username']
        password = request.form['password']
        logging.info(f"[{formatted_time}] Attacker IP: {ip} tried to login with Username: {username}, Password: {password}")
        flash("Incorrect username or password.", "error")
        return render_template('fakeLogin.html')

    return render_template('fakeLogin.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
