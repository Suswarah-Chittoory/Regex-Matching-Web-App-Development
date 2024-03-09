import re
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("signin.html")

name = ""

@app.route('/regex', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        global name
        id = request.form.get('id')
        if re.findall(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', id):
            if re.findall(r'^([a-zA-Z]+)', id):
                name = re.findall(r'^([a-zA-Z]+)', id)[0]
                name = f"Welcome {name.capitalize()}..."
            else:
                name = "Welcome..."
            return render_template("home.html", name=name)
        elif id == "":
            name = "Please enter your email"
            return render_template("signin.html", name=name)
        else:
            name = "Enter a valid email id"
            return render_template("signin.html", name=name)
    elif request.method == "GET":
        return render_template("home.html", name=name)
    else:
        return redirect(url_for('home'))

@app.route('/results', methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        note = request.form.get("note")
        testnote = request.form.get('testnote')
        output = ""
        if note and testnote:
            if len(re.findall(note, testnote)) == 0:
                output = "Your regular expression does not match the subject string."
            else:
                regex = re.findall(note, testnote)
                output = f'Matched result: {regex}'
        else:
            output = "Please enter valid input"
        return render_template("home.html", output=output, name=name)
    elif request.method == "GET":
        return render_template("home.html", output=output, name=name)
    else:
        return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)