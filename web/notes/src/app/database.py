import sqlite3
import bcrypt

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    print('[+] Initializing database')
    conn = get_db_connection()
    with conn:
        conn.executescript(f'''
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS notes;
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username INTEGER NOT NULL,
            note TEXT NOT NULL
        )
''')
        
    conn.close()
    
def add_user(username, password):
    conn = get_db_connection()
    with conn:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        conn.executescript(f'''
                           INSERT INTO users (username, password) VALUES ('{username}', '{password_hash}')
        ''')
    conn.close()
    
def get_user(username) -> dict:
    conn = get_db_connection()
    with conn:
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user

def login_user(username, password:str):
    user = get_user(username)
    if not user:
        return False
    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return user
    return False

def get_notes(username):
    conn = get_db_connection()
    with conn:
        notes = conn.execute('SELECT * FROM notes WHERE username = ?', (username,)).fetchall()
    conn.close()
    return notes

def get_note_by_id(note_id):
    conn = get_db_connection()
    with conn:
        note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    conn.close()
    return note

def add_note(username, note):
    conn = get_db_connection()
    with conn:
        conn.execute('INSERT INTO notes (username, note) VALUES (?, ?)', (username, note))
    conn.close()
    
def delete_note_by_id(note_id):
    conn = get_db_connection()
    with conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.close()
    
def edit_note_by_id(note_id, new_note):
    conn = get_db_connection()
    with conn:
        conn.execute('UPDATE notes SET note = ? WHERE id = ?', (new_note, note_id))
    conn.close()
    
    