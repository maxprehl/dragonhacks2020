import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


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

<<<<<<< HEAD
	return render_template('Account.html', title = title , paragraph = paragraph)

@app.route('/Learning')
def Learning():
	
	title = "Learning"
	paragraph = ["Do you want to learn on your own or with other people?"]
	
	return render_template('learning.html', title = title , paragraph = paragraph)
=======
	title = "Account"
	paragraph = ["User Account Information"]

	return render_template('Account.html', title=title, paragraph=paragraph)


@app.route('/Learning')
def Learning():
>>>>>>> c68ce25a79aee7a468ac4f8d4a04e016e9ff5ff3

	title = "Learning"
	paragraph = ["Do you want to learn on your own or with other people?"]

	return render_template('learning.html', title=title, paragraph=paragraph)

    # Have two options for if the person wants to learn on their own or with other people
    # Option1 = Individual Learning
    # Option2 = Community Learning


if __name__ == "__main__":
    app.run(debug=True)
