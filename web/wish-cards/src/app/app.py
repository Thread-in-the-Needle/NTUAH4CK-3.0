from flask import Flask, request, render_template, send_file
import io
from functools import wraps
app = Flask(__name__)
from util import cards, make_card, ADMINPASS
import os

try:    secret_wish = open('flag.txt','r').read().strip()
except: secret_wish='NH4CK{secrettttt}'


def local(f):
    @wraps(f)
    def check(*args, **kwargs):
        if request.remote_addr != '127.0.0.1':
            return render_template('error.html', error= 'Sorry, this page is not available for the public 🥲')
        return f(*args, **kwargs)
    return check


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/<path:path>')
def catch_all(path):
    return render_template('error.html', error= f'Page not found 🤔🤔🤔')
    

@app.route('/cards', methods= ['GET', 'POST'])
def card():
    if 'image' not in request.values:
        return render_template('cards.html', cards= cards)
    image = request.values.get('image')
    card = make_card(image)
    if not card:
        return render_template('error.html', error= 'Invalid image 😢')
    return send_file(io.BytesIO(card), mimetype= 'image/png', as_attachment= True, download_name= 'card.png')
       
@app.route('/custom-cards', methods=['GET', 'POST'])
@local
def custom_card():
    if 'image' not in request.values:
        return render_template('custom-cards.html', cards= cards)
    image = request.values.get('image')
    wish = request.values.get('wish')
    card = make_card(image, wish)
    if not card:
        return render_template('error.html', error= 'Invalid image 😢')
    return send_file(io.BytesIO(card), mimetype= 'image/png', as_attachment= True, download_name= 'card.png')
      
        
@app.route('/admin-card')
@local
def admin():
    passw = request.args.get('pass', '')
    if passw != ADMINPASS:
        return render_template('error.html', error= 'Urm, wrong password ❌')
    secret_card = make_card('colors.png', wish= f'Merry Xmas, don\'t share my secret: {secret_wish}')
    return send_file(io.BytesIO(secret_card), mimetype= 'image/png', as_attachment= True, download_name= 'flag.png')
    

    
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 1337, threaded= True, debug= True)