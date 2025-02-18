from flask import Flask, render_template, request, redirect

app = Flask(__name__)

valid_username = "user"
valid_password = "password"

@app.route('/')
def home():
    return render_template('login.html')  

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == valid_username and password == valid_password:
        return f"Welcome, {username}!"  
    else:
        return redirect("http://127.0.0.1:5001/fake-login")

if __name__ == "__main__":
    app.run(debug=True, port=5000)  
