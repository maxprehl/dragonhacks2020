import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def homepage():

	title = "Homepage"
	paragraph = [""]

	return render_template('index.html', title = title, paragraph = paragraph)

@app.route('/')
def tips():
	
	title = ""
	paragraph = [""]

	return render_template('.html', title = title, paragraph = paragraph)

@app.route('/')
def community():

	title = ""
	paragraph = [""]

	return render_template('.html', title = title, paragraph = paragraph)

if __name__ == "__main__":
	app.run(debug=True)app = Flask(__name__, instance_relative)

