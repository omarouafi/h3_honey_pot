import logging
import time
from flask import Flask, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure logging to include timestamps
logging.basicConfig(
    filename="honeypot_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",  # Adds a timestamp to logs
    datefmt="%Y-%m-%d %H:%M:%S"
)

@app.route('/fake-login', methods=['GET', 'POST'])
def fake_login():
    current_time = time.time()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))  # Human-readable format

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
    app.run(debug=True, port=5001)
