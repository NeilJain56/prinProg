import sys

from flask import Flask, render_template, request, redirect, Response
from flask_cors import CORS, cross_origin

from personalEandD import personalEncryption
from personalEandD import personalDecryption
import random, json

app = Flask(__name__)
cors = CORS(app, resources={r"/encrypt": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'

import base64



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
	final = caesar(baseString)
	print('string received is ', baseString)
	return final
	#return '''Woohoo'''

def caesar(baseString):
	finalString = ''
	for c in baseString:
		if c == 'a' or c == 'A':
				finalString += 'c'
		if c == 'b' or c == 'B':
				finalString += 'd'
		if c == 'c' or c == 'C':
				finalString += 'e'
		if c == 'd' or c == 'D':
				finalString += 'f'
		if c == 'e' or c == 'E':
				finalString += 'g'
		if c == 'f' or c == 'F':
				finalString += 'h'
		if c == 'g' or c == 'G':
				finalString += 'i'
		if c == 'h' or c == 'H':
				finalString += 'j'
		if c == 'i' or c == 'I':
				finalString += 'k'
		if c == 'j' or c == 'J':
				finalString += 'l'
		if c == 'k' or c == 'K':
				finalString += 'm'
		if c == 'l' or c == 'L':
				finalString += 'n'
		if c == 'm' or c == 'M':
				finalString += 'o'
		if c == 'n' or c == 'N':
				finalString += 'p'
		if c == 'o' or c == 'O':
				finalString += 'q'
		if c == 'p' or c == 'P':
				finalString += 'r'

		if c == 'q' or c == 'Q':
				finalString += 's'

		if c == 'r' or c == 'R':
				finalString += 't'

		if c == 's' or c == 'S':
				finalString += 'u'

		if c == 't' or c == 'T':
				finalString += 'v'

		if c == 'u' or c == 'U':
				finalString += 'w'
		if c == 'v' or c == 'V':
				finalString += 'x'
		if c == 'w' or c == 'W':
				finalString += 'y'
		if c == 'x' or c == 'X':
				finalString += 'z'
		if c == 'y' or c == 'Y':
				finalString += 'a'
		if c == 'z' or c == 'Z':
				finalString += 'b'
		if c == ' ':
				finalString += '_'
	return finalString


@app.route('/decrypt')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def decrypt():
	baseString = request.args.get('str') # is no data sent this will return null
	final = anticaesar(baseString)
	print('string received is ', baseString)
	return final
	#return '''Woohoo'''

def anticaesar(baseString):
	finalString = ''
	for c in baseString:
		if c == 'a' or c == 'A':
				finalString += 'y'
		if c == 'b' or c == 'B':
				finalString += 'z'
		if c == 'c' or c == 'C':
				finalString += 'a'
		if c == 'd' or c == 'D':
				finalString += 'b'
		if c == 'e' or c == 'E':
				finalString += 'c'
		if c == 'f' or c == 'F':
				finalString += 'd'
		if c == 'g' or c == 'G':
				finalString += 'e'
		if c == 'h' or c == 'H':
				finalString += 'f'
		if c == 'i' or c == 'I':
				finalString += 'g'
		if c == 'j' or c == 'J':
				finalString += 'h'
		if c == 'k' or c == 'K':
				finalString += 'i'
		if c == 'l' or c == 'L':
				finalString += 'j'
		if c == 'm' or c == 'M':
				finalString += 'k'
		if c == 'n' or c == 'N':
				finalString += 'l'
		if c == 'o' or c == 'O':
				finalString += 'm'
		if c == 'p' or c == 'P':
				finalString += 'n'

		if c == 'q' or c == 'Q':
				finalString += 'o'

		if c == 'r' or c == 'R':
				finalString += 'p'

		if c == 's' or c == 'S':
				finalString += 'q'

		if c == 't' or c == 'T':
				finalString += 'r'

		if c == 'u' or c == 'U':
				finalString += 's'
		if c == 'v' or c == 'V':
				finalString += 't'
		if c == 'w' or c == 'W':
				finalString += 'u'
		if c == 'x' or c == 'X':
				finalString += 'v'
		if c == 'y' or c == 'Y':
				finalString += 'w'
		if c == 'z' or c == 'Z':
				finalString += 'x'
		if c == '_':
				finalString += ' '
	return finalString


@app.route('/encrypt1')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def encrypt1():
	baseString = request.args.get('str') # is no data sent this will return null
	reversed = reverse(baseString)
	print('string received is ', baseString)
	return reversed
	#return '''Woohoo'''

def reverse(baseString):
	return baseString[::-1]

@app.route('/decrypt1')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def decrypt1():
	baseString = request.args.get('str') # is no data sent this will return null
	reversed = reverse(baseString)
	print('string received is ', baseString)
	return reversed
	#return '''Woohoo'''



@app.route('/encrypt2')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def encrypt2():
	baseString = request.args.get('str') # is no data sent this will return null
	
	final = encode('notsosecretkey' ,baseString)
	print('string received is ', baseString)
	return final
	#return '''Woohoo'''

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

@app.route('/decrypt2')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def decrypt2():
	baseString = request.args.get('str') # is no data sent this will return null
	
	final = decode("notsosecretkey" ,baseString)
	print('string received is ', baseString)
	return final
	#return '''Woohoo'''

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

@app.route('/encrypt3')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def encrypt3():
	baseString = request.args.get('str') # is no data sent this will return null
	
	final = personalEncryption(baseString)
	print('string received is ', baseString)
	return final



@app.route('/decrypt3')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def decrypt3():
	baseString = request.args.get('str') # is no data sent this will return null
	
	final = personalDecryption(baseString)
	print('string received is ', baseString)
	return final


if __name__ == '__main__':
	# run!
	app.run()