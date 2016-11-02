# -*- coding:utf-8 -*-
import redis

class redisQueue(object):

    redisConn = None
    __instance = None

    def __init__(self,queueName):
        if self.redisConn is None:
            self.redisConn = redis.StrictRedis(host='localhost',port=6379)
        self.queueName = queueName

    def __new__(cls,*kw,**args):
        if redisQueue.__instance is None:
            redisQueue.__instance = object.__new__(cls,*kw,**args)
        return redisQueue.__instance

    def inQueue(self,request):
        # token = request.form['token']
        # team_id = request.form['team_id']
        # team_domain = request.form['team_domain']
        # channel_id = request.form['channel_id']
        # channel_name = request.form['channel_name']
        # timestamp = request.form['timestamp']
        # user_id = request.form['user_id']
        # user_name = request.form['user_name']
        text = request.form['text']
        # trigger_word = request.form['trigger_word']

        if self.redisConn.sadd(self.queueName,text) is not None:
            return True
        return False

    def popQueue(self):
        memeber = self.redisConn.spop(self.queueName)
        if memeber is not None:
            return memeber
        else:
            return None
