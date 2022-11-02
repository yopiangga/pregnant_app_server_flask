from typing import Type
from urllib import response
from flask_cors import CORS,cross_origin
from flask import Flask,render_template, request
import numpy as np

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
# @cross_origin()
def home():
    return "home"

if __name__ == '__main__':
   app.run(debug=True)