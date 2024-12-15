from flask import Flask, request, render_template, send_file, session, redirect, url_for, flash
from functools import wraps
from os import environ
import subprocess
app = Flask(__name__)

app.secret_key = environ.get('APP_SECRET_KEY',b'asldfjasfkl')

try:    FLAG = open('flag.txt','r').read().strip()
except: FLAG = 'NH4CK{FAKE_FLAG}'

BAD_CHARS = '/<>\\{}'

import database

database.init_db()

from bot import Bot

def bad(s):
    return any(c in BAD_CHARS for c in s)

def is_local(request):
    return request.remote_addr == '127.0.0.1'

def logged_in(f):
    @wraps(f)
    def check(*args, **kwargs):
        if not is_local(request) and 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return check

@app.route('/test/')
def test():
    return '<script>console.log("XSS")</script>'


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('notes'))
    return redirect(url_for('login'))
    
    
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    return render_template('error.html', error= f'Page not found 🤔🤔🤔')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # POST:
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username or not password:
        flash('Username and Password are required')
        return render_template('login.html')
    try:
        user = database.login_user(username, password)
    except Exception as e:
        flash(f'An error occurred: {e}')
        return render_template('login.html')
    if not user:
        flash('Invalid Username or Password')
        return render_template('login.html')
    session['username'] = user['username']
    return redirect(url_for('notes'))
    
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # POST:
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username or not password:
        flash('Username and Password are required')
        return render_template('register.html')
    if database.get_user(username):
        flash('Username already exists')
        return render_template('register.html')
    try:
        database.add_user(username, password)
        flash('User registered successfully')
        render_template('login.html')
    except Exception as e:
        flash(f'An error occurred: {e}')
    return render_template('register.html')
    
    
@app.route('/logout/')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))    
    
@app.route('/notes/', methods=['GET'])
@logged_in
def notes():
    notes = database.get_notes(session['username'])
    return render_template('notes.html', note_ids = [note['id'] for note in notes])
    
@app.route('/notes/<int:note_id>/', methods=['GET'])
@logged_in
def note_detail(note_id):
    note = database.get_note_by_id(note_id)
    if not note:
        return render_template('error.html', error= 'Note not found')
    if not is_local(request) and note['username'] != session['username'] :
        return render_template('error.html', error= 'Hey, this is not your note 🤨')
    return render_template('note.html', note= note)
    
@app.route('/notes/new/', methods=['GET','POST'])
@logged_in
def new_note():
    if request.method == 'GET':
        return render_template('new_note.html')
    # POST:
    note = request.form.get('note', '')
    if not note:
        return render_template('error.html', error= 'No note provided')
    if bad(note):
        return render_template('error.html', error= 'Invalid characters in note')
    database.add_note(session['username'], note)
    return redirect(url_for('notes'))

    
@app.route('/notes/delete/<int:note_id>/', methods=['POST'])
@logged_in
def delete_note(note_id):
    note = database.get_note_by_id(note_id)
    if not note:
        return render_template('error.html', error= 'Note not found')
    if not is_local(request) and note['username'] != session['username'] :
        return render_template('error.html', error= 'Hey, this is not your note 🤨')
    database.delete_note_by_id(note_id)
    return redirect(url_for('notes'))
    
@app.route('/notes/edit/<int:note_id>/', methods=['GET','POST'])
@logged_in
def edit_note(note_id):
    if request.method == 'GET':
        note = database.get_note_by_id(note_id)
        if not note:
            return render_template('error.html', error= 'Note not found')
        if not is_local(request) and note['username'] != session['username']:
            return render_template('error.html', error= 'Hey, this is not your note 🤨')
        return render_template('edit_note.html', note= note, note_id= note_id)
    # POST:
    note = database.get_note_by_id(note_id)
    if not note:
        return render_template('error.html', error= 'Note not found')
    if note['username'] != session['username'] and not is_local(request):
        return render_template('error.html', error= 'Hey, this is not your note 🤨')
    new_note = request.form.get('note', '')
    if not new_note:
        return render_template('error.html', error= 'No note provided')
    if bad(new_note):
        return render_template('error.html', error= 'Invalid characters in note')
    database.edit_note_by_id(note_id, new_note)
    return redirect(url_for('notes'))
    

@app.route('/notes/export_latex/<int:note_id>/')
def export_latex(note_id:int):
    if not is_local(request):
        flash('This functionality is disabled for remote users, until we fix some security issues')
        return redirect(url_for('note_detail', note_id= note_id))
    if not note_id:
        return render_template('error.html', error= 'Note ID is required')
    note = database.get_note_by_id(note_id)
    if not note:
        return render_template('error.html', error= 'Note not found')
    output_pdf_path = generate_pdf(note['note'])
    if output_pdf_path.startswith('Error'):
        return output_pdf_path, 500
    return send_file(output_pdf_path, as_attachment= True)
    
    
@app.route('/notes/report_note/<int:note_id>/', methods=['POST'])
@logged_in
def report_note(note_id):
    if not note_id:
        return render_template('error.html', error= 'Note ID is required')
    note = database.get_note_by_id(note_id)
    if not note:
        return render_template('error.html', error= 'Note not found')
    if note['username'] != session['username']:
        return render_template('error.html', error= 'Not your note to report')
    bot = Bot()
    bot.visit(f'http://127.0.0.1:1337/notes/{note_id}/')
    bot.close()
    flash('Note reported successfully')
    return redirect(url_for(f'note_detail', note_id= note_id))
    


def generate_pdf(latex_code):
    if any(c in BAD_CHARS for c in latex_code):
        return f"Error: Sorry `{BAD_CHARS}` are disallowed for now 😥"

    filename = "/opt/app/input.tex"
    
    with open(filename, "w") as f:
        f.write(latex_code)
    
    process = subprocess.Popen(["pdflatex", "-interaction=nonstopmode", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode !=0:
        return f"Error: PDF generation failed:\n {output.decode()}"
    
    return 'input.pdf'
    
    

    
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 1337, threaded= True, debug= True)
    