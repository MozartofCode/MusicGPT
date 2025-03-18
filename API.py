from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


@app.route('/')
def home():
    return "Welcome to the API"

if __name__ == '__main__':
    app.run(debug=True)
