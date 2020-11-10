from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['uname']
        return redirect(url_for('user', usr=user ))
    else:
        return render_template('login.html')

@app.route("/test")
def test():
    db.db.collection.insert_one({"name": 'Mini'})
    return "Connected to the data base!"


@app.route('/register', methods = ['POST', 'GET'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)