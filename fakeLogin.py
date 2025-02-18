import logging
from flask import Flask, render_template, request

app = Flask(__name__)

logging.basicConfig(filename="honeypot_logs.txt", level=logging.INFO)

@app.route('/fake-login', methods=['GET', 'POST'])
def fake_login():
    if request.method == 'POST':
        ip = request.remote_addr
        username = request.form['username']
        password = request.form['password']
        
        logging.info(f"Attacker IP: {ip} tried to login with Username: {username}, Password: {password}")
        
        return "Incorrect username or password."  
    
    return render_template('fakeLogin.html')  

if __name__ == "__main__":
    app.run(debug=True, port=5001)  
