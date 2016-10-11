# -*- coding:utf-8 -*-

# ojService 是一个服务，在这个平台内会有很多服务，根据slack信息来进行解析和进行service
import sys
sys.path.append('..')
import funtools.mailTool as mt
class ojService(object):
    def __init__(self):
        pass

    # example
    def sendAction(self,msgList):
        if msgList is None:
            return [0,'参数为空']
        mailConfig = {
            "mailAccount":"zuston@sina.cn",
            "mailPwd":"12267020zjf",
            "smtpServer":"smtp.sina.cn",
            "popServer":"pop.sina.cn",
            "sendAddr":"731673917@qq.com",
            "subject":"love"
        }
        mail = mt.mailTool(mailConfig)
        mail.sendMail(str(msgList))
        return [1,'ok']


    def testAction(self,paramList=[]):
        print 'this is the ojService'
        return [1,'ok']
