from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

"""@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    username = request.form['username']

    return render_template('welcome.html', username=username)"""

@app.route("/input", methods=["GET", 'POST'])
def input_data():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    success = 0

    while success < 1:
        success = 1
        if username == "" or " " in username or len(username) < 3 or len(username) > 20:
            username_error = "Please submit a valid username"
            success = 0
        else:
            username_error = ""

        if password == "" or " " in password or len(password) < 3 or len(password) > 20:
            password_error = "Please submit a valid password"
            success = 0
        else:
            password_error = ""

        if password != verify_password:
            verify_error = "Your passwords do not match"
            success = 0
        else:
            verify_error = ""

        if email != "":
            if ("@" not in email) or ("." not in email) or (" " in email) or len(password) < 3 or len(password) > 20:
                email_error = "Your email is invalid"
                success = 0
        else:
            email_error = ""

        if success == 0:
            return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
        else:
            return render_template('welcome.html', username=username)

@app.route("/", methods=["GET", 'POST'])
def index():
    return render_template('index.html')

app.run()