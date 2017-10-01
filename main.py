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

    if username == "":
        error = "Please submit a username"
        return redirect("/?error=" + error)
    elif " " in username: 
        error = "Usernames cannot contain invalid characters"
        return redirect("/?error=" + error)
    elif len(username) < 3 or len(username) > 20:
        error = "Usernames must be longer than 3 and shorter than 20 characters"
        return redirect("/?error=" + error)

    else:
        return render_template('welcome.html', username=username)

@app.route("/", methods=["GET", 'POST'])
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()