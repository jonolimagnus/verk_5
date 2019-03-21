from flask import Flask, flash, redirect, request
from flask import json
import os
from datetime import datetime
from flask import render_template
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run()
