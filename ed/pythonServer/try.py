import sys

from flask import Flask, render_template, request, redirect, Response
from flask_cors import CORS, cross_origin

import random, json

app = Flask(__name__)
cors = CORS(app, resources={r"/encrypt": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
	# serve index template
	return render_template('manifest.json')

@app.route('/hello')
def hello():
	return "Hello World"

@app.route('/encrypt')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def encrypt():
	baseString = request.args.get('str') # is no data sent this will return null
	print('string received is ', baseString)
	return baseString
	#return '''Woohoo'''

@app.route('/decrypt')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def decrypt():
	baseString = request.args.get('str') # is no data sent this will return null
	print('string received is ', baseString)
	return baseString
	#return '''Woohoo'''

@app.route('/encrypt1')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def encrypt1():
	baseString = request.args.get('str') # is no data sent this will return null
	print('string received is ', baseString)
	return baseString
	#return '''Woohoo'''

@app.route('/decrypt1')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def decrypt1():
	baseString = request.args.get('str') # is no data sent this will return null
	print('string received is ', baseString)
	return baseString
	#return '''Woohoo'''

if __name__ == '__main__':
	# run!
	app.run()