import os
import sqlite3
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from contextlib import closing

# configuration
DATABASE = './data/LLL.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
Bootstrap(app)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('data/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def Login():

    title = "Login"
    paragraph = ["Login to your account."]

    return render_template('login.html', title=title, paragraph=paragraph)


@app.route('/Signup')
def Signup():

    title = "Signup"
    paragraph = ["Create an account."]

    return render_template('signup.html', title=title, paragraph=paragraph)


@app.route('/Account')
def Account():

    title = "Account"
    paragraph = ["User Account Information"]

    return render_template('Account.html', title=title, paragraph=paragraph)


@app.route('/Learning')
def Learning():

    title = "Learning"
    paragraph = ["Do you want to learn on your own or with other people?"]

    return render_template('learning.html', title=title, paragraph=paragraph)

    # Have two options for if the person wants to learn on their own or with other people
    # Option1 = Individual Learning
    # Option2 = Community Learning


if __name__ == "__main__":
    app.run(debug=True)
