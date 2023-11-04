from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api():
    data = {'message': f"This is a sample Flask REST API! - {os.getenv('key1')}"}
    return jsonify(data)
