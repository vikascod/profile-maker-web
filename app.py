from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/design')
def design():
    return render_template("design.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == ['POST']:
        firstname = request.form('firstname')
        lastname = request.form('lastname')
        Email = request.form('email')
        phone = request.form('phone')
        schoolname = request.form('schoolname')
        collagename = request.form('collagename')
        about = request.form('about')
        
    return "Your Postfolio has been Uploaded"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        fullname = request.form('fullname')
        email = request.form('email')
        password1 = request.form('password1')
        password2 = request.form('password2')
    return render_template("design.html")

if __name__ == '__main__':
    app.run(debug=True)