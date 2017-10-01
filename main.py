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

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
        error = "Please submit a valid username"
        return redirect("/?error=" + error)

    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
        error = "Please submit a valid password"
        return redirect("/?error=" + error)

    if password != verify_password:
        error = "Your passwords do not match"
        return redirect("/?error=" + error)

    if email != "":
        if ("@" not in email) or ("." not in email) or (" " in email) or len(password) < 3 or len(password) > 20:
            error = "Your email is invalid"
            return redirect("/?error=" + error)
    
    else:
        return render_template('welcome.html', username=username)

@app.route("/", methods=["GET", 'POST'])
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()