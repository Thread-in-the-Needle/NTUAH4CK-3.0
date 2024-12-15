from flask import Flask ,render_template,request,make_response
app = Flask(__name__)
import os

FLAG = open('flag.txt','r').read().strip()

@app.route('/')
def index():
    
    resp = make_response(render_template('index.html'))
    cookies = request.cookies
    if 'user' not in cookies:
        resp.set_cookie('user', 'guest')
    return resp
    
@app.route('/<path:path>')
def catch_all(path):
    resp = make_response(render_template('error.html',error=f'Page not found 😶‍🌫️'))
    cookies = request.cookies
    if 'user' not in cookies:
        resp.set_cookie('user', 'guest')
    return resp
        
    
@app.route('/admin', methods=['GET'])
def admin():
    cookies = request.cookies
    err_resp = make_response(render_template('error.html',error=f'You are not authorized to view this page 🔒😡🔒'))
    err_resp.set_cookie('user', 'guest')
    if cookies.get('user', None) == 'admin':
        return render_template('admin.html',flag=FLAG)
    return err_resp
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1337, threaded=True, debug=True)