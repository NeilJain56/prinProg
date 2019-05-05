import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def index():
	# serve index template
	return render_template('manifest.json')

@app.route('/hello')
def hello():
	return "Hello World"

if __name__ == '__main__':
	# run!
	app.run()