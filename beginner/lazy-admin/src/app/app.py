from flask import Flask, request ,render_template,redirect,url_for
app = Flask(__name__)
from bot import Bot
from urllib.parse import quote


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return render_template('error.html',error=f'Page not found 😶‍🌫️')
    

@app.route('/search')
def search():
    return render_template('search.html')
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    if request.method == 'POST':
        msg = request.form.get('msg', None)
        if not msg:
            return render_template('contact.html',error=True)
        
        # Simulate an admin reading the message
        url=f'http://127.0.0.1:1337/msg?message={quote(msg)}'
        bot=Bot()
        bot.visit(url)
        bot.close()
        return render_template('contact.html',success=True)
    
    
@app.route('/msg', methods=['GET']) # This is the endpoint that the admin (bot) will visit
def msg():
    if request.remote_addr!='127.0.0.1':
        return render_template('error.html',error=f'Unauthorized access 😶‍🌫️')
    msg=request.args.get('message','')
    return render_template('msg.html',message=msg)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1337, threaded=True, debug=True)