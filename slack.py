from flask import Flask,url_for,request
import funtools.redisQueue as rq
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

# accept the slack message
@app.route('/slack',methods=['POST','GET'])
def slack():
    redisQ=rq.redisQueue()
    # redisQ.inQueue(request)
    print redisQ.test()
    return 'slack response'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
