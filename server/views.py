from flask import Flask, render_template
from server import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

