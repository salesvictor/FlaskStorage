from app import app
from flask import render_template, request, redirect, url_for, make_response, session

@app.route('/')
def index():
  if not 'username' in session or not request.cookies.get('username'):
    return render_template('index.html')

  return redirect(url_for('store'))

@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
  if request.method == 'POST':
    username = request.form.get('username')

    response = make_response(redirect(url_for('store')))
    response.set_cookie('username', username)

    return response

  return render_template('form.html')

@app.route('/sessions', methods=['GET', 'POST'])
def sessions():
  if request.method == 'POST':
    session['username'] = request.form.get('username')
    return redirect(url_for('store'))

  return render_template('form.html')

@app.route('/store')
def store():
  return 'store'
