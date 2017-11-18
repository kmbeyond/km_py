# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:59:17 2017

@author: SZTJC5
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

app.run(port=5000)
