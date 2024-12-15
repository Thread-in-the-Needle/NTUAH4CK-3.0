from data import cards, wishes
from random import choice
import imgkit
from requests import get
from base64 import b64encode, b64decode
from flask import render_template_string

try:    ADMINPASS = open('adminpass.txt').read().strip()
except: ADMINPASS = 'adminpass'

def get_wish():
    return choice(wishes)

def img_from_url(url):
    r = get(url)
    if r.status_code != 200:
        return None
    return b64encode(r.content).decode()

def generate_card_html(b64_image, wish):
    card_html = f'''
    <html>
    <head>
        <style>
            .card {{
                width: 800px;
                height: 600px;
                background-image: url(data:image/png;base64,{b64_image});
                background-size: cover;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 20px;
                text-align: center;
                padding: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            {wish}
        </div>
    </body>
    </html>
    '''
    return render_template_string(card_html, **globals())

def make_card(img: str, wish= ''):
    if not img or not img.endswith('.png'):
        return None
    if any([c in wish for c in '<>%_&"\\()']): # these may crash something
        return None
    
    if not wish:
        wish = get_wish()
    
    img_b64 = img_from_url(f'http://127.0.0.1:1337/static/images/{img}')
    if not img_b64:
        return None
    card_html = generate_card_html(img_b64,wish)
    as_pic = imgkit.from_string(card_html, False, options= {'format': 'png', 'quiet': '', 'crop-h': '1000', 'crop-w': '800'})
    return as_pic
    