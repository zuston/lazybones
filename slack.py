from flask import Flask,url_for,request
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/slack',methods=['POST','GET'])
def slack():
    print request.form['text']
    return 'slack response'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
