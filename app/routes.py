from flask import render_template, request, redirect, url_for, make_response, session, send_from_directory
from werkzeug.utils import secure_filename
from . import app
import os

@app.route('/download/<path:filename>')
def download(filename):
  return send_from_directory(os.path.join(os.path.pardir, app.config['UPLOAD_FOLDER']), filename)

@app.route('/')
def index():
  if 'username' in session or 'username' in request.cookies:
    return redirect(url_for('home'))

  return render_template('index.html')

@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
  if session.get('username'):
    return redirect(url_for('home'))

  if request.method == 'POST':
    username = request.form.get('username')

    response = make_response(redirect(url_for('home')))
    response.set_cookie('username', username)

    return response

  return render_template('login_form.html')

@app.route('/sessions', methods=['GET', 'POST'])
def sessions():
  if request.cookies.get('username'):
    return redirect(url_for('home'))

  if request.method == 'POST':
    session['username'] = request.form.get('username')
    return redirect(url_for('home'))

  return render_template('login_form.html')

@app.route('/home')
def home():
  username = request.cookies.get('username') or session.get('username')

  if not username:
    return redirect(url_for('index'))

  return render_template('home.html', username=username)

@app.route('/logout')
def logout():
  response = make_response(redirect(url_for('index')))

  session.pop('username', None)
  response.delete_cookie('username')
    
  return response

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
  if request.method == 'POST':
    uploaded_files = request.files.getlist('files')

    for uploaded_file in uploaded_files:
      if allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('view_files'))

  return render_template('upload_form.html')

@app.route('/files')
def view_files():
  files = os.listdir(app.config['UPLOAD_FOLDER'])
  return render_template('view_files.html', files=files)
