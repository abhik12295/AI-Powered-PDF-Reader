from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from supabase import Client, create_client

app = Flask(__name__)
CORS(app)

SUPERBASE_URL = os.environ.get('SUPERBASE_URL')
SUPERBASE_KEY = os.environ.get('SUPERBASE_KEY')

supabase:Client = create_client(SUPERBASE_URL, SUPERBASE_KEY)

def create_user(email, password):
    endpoint = f'{SUPERBASE_URL}/auth/v1/signup'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(endpoint, json=data)
    return response.json()

def login_user(email, password):
    endpoint = f'{SUPERBASE_URL}/auth/v1/token?grant_type=password'
    headers = {
        "apikey": SUPERBASE_KEY,
        "Content-Type": "application/json"
    }
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()

@app.route('/signup', methods = ['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response = create_user(email, password)
    return jsonify(response)

@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response = login_user(email, password)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)