from flask import Flask, request ,render_template,redirect,url_for
import util
app = Flask(__name__)
from bot import Bot
from urllib.parse import quote

app.config['DEBUG'] = False
app.config['MAX_FORM_PARTS'] = 100

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/<path:path>')
def catch_all(path):
    return render_template('error.html',error=f'Page not found 😶‍🌫️')
    

@app.route('/search', methods=['GET', 'POST'])
def search():
    prev_searches=util.get_prev_searches()[::-1] # latest first
    if request.method == 'GET':
        return render_template('search.html',prev_searches=prev_searches)
    if request.method == 'POST':
        form_dict = request.form.to_dict()
        queries=list(form_dict.values())
        if not queries:
            return render_template('search.html',error=True,prev_searches=prev_searches)
        items = util.search(queries)
        util.add(items)
        return render_template('search.html',search=items,prev_searches=prev_searches)
    
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
