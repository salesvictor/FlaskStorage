from app import app
from flask import render_template

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cookies')
def cookies():
  return 'cookies'

@app.route('/sessions')
def sessions():
  return 'sessions'
