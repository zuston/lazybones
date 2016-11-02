from flask import Flask,url_for,request
import component.tools.redisQueue as rq
import logging
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/slack',methods=['POST','GET'])
def slack():
    redisQ=rq.redisQueue('zqueue')
    if redisQ.inQueue(request):
        logging.info('accept successfully')
    else:
        logging.error('error text:[%s]'%request.form['text'])
    return 'ok'

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./log/server.log',
                        filemode='w')
    app.debug = True
    app.run(host='0.0.0.0')
