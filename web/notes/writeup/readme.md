# Overview
- The website is a note taking app.
- It disallows `BAD_CHARS = '/<>\\{}'` in the note's content.
- There is an `export` feature that exports a latex file of the note. This feature is disabled to external users.
- The flag is in the `flag.txt` file, so we need some kind of file read vulnerability to get the flag. This could be done through the `export` feature, if we find a way to bypass the `BAD_CHARS` filter.
- Analyzing the source code, we first find that `add_user` function is vulnerable to SQL stacked queries injection.
```python
def add_user(username, password):
    conn = get_db_connection()
    with conn:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        conn.executescript(f'''
                           INSERT INTO users (username, password) VALUES ('{username}', '{password_hash}')
        ''')
    conn.close()
```
- There is also a `report_note` feature that allows users to report notes. There is an admin bot that visits the reported notes.

# Solution
- We will perform the following chain of attacks:
    - SQLi to insert a note with a xss payload.
    - SQLi to insert a note with a Latex LFI payload, (use hex encoding to bypass the `BAD_CHARS` filter).
    - XSS to make the admin bot use the export function, and then put the pdf content in a note.
    - Retrieve the note with the flag pdf.
  
- View the [exploit script](solve.py) script for the full exploit code.