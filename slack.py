from flask import Flask,url_for,request
import funtools.redisQueue as rq
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

# accept the slack message
@app.route('/slack',methods=['POST','GET'])
def slack():
    redisQ=rq.redisQueue('zqueue')
    if redisQ.inQueue(request):
        print 'accept the request and save the queue successfully'
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
