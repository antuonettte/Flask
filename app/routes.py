from werkzeug.utils import redirect
from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/updates')
def updates():
    return render_template('updates.html')

@app.route('/info')
def info():
    return render_template('info.html')