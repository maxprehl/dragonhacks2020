import os
import sqlite3
import json
from flask import Flask, render_template, g, redirect, url_for
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
    return sqlite3.connect(DATABASE)


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('data/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def fill_db():
    with closing(connect_db()) as db:
        with open('data/songs.json') as json_file:
            data = json.load(json_file)
            for song in data['song_info']:
                db.cursor().execute("insert into songs values (?, ?, ?, ?, ?)",
                                    [None, song['song_name'], song['unique_words'], song['match_words'], song['max_words']])
                db.commit()
        with open('data/users.json') as json_file2:
            data2 = json.load(json_file2)
            for user in data2['user_info']:
                db.cursor().execute("insert into users values (?, ?, ?, ?, ?)",
                                    [None, user['name'], user['password'], user['main_language'], user['want_language']])
                db.commit()


@app.route('/')
def Login():

    title = "Login"
    paragraph = ["Login to your account."]

    return render_template('login.html', title = title, paragraph = paragraph)


@app.route('/signin')
def Signup():

    title = "Signup"
    paragraph = ["Create an account."]

    return render_template('signin.html', title = title, paragraph = paragraph)


@app.route('/account')
def Account():

	title = "Account"
	paragraph = ["User Account Information"]

	return render_template('account.html', title=title, paragraph=paragraph)


@app.route('/learning')
def Learning():

	title = "Learning"
	paragraph = ["Do you want to learn on your own or with other people?"]

	return render_template('learning.html', title=title, paragraph=paragraph)

    # Have two options for if the person wants to learn on their own or with other people
    # Option1 = Individual Learning
    # Option2 = Community Learning


if __name__ == "__main__":
    app.run(debug=True)
