# -*- coding:utf-8 -*-

# ojService 是一个服务，在这个平台内会有很多服务，根据slack信息来进行解析和进行service
import sys
sys.path.append('..')
import funtools.mailTool as mt
class ojService(object):
    def __init__(self):
        pass

    def send(self,msgList):
        # self.mailAccount = mailConfig['mailAccount']
        # self.mailPwd = mailConfig['mailPwd']
        # self.smtpServer = mailConfig['smtpServer']
        # self.popServer = mailConfig['popServer']
        # self.sendAddr = mailConfig['sendAddr']
        # self.subject = mailConfig['subject']
        mailConfig = {
            "mailAccount":"zuston@sina.cn",
            "mailPwd":"12267020zjf",
            "smtpServer":"smtp.sina.cn",
            "popServer":"pop.sina.cn",
            "sendAddr":"731673917@qq.com",
            "subject":"love"
        }
        mail = mt.mailTool(mailConfig)
        return mail.sendMail(msgList[0])

    def test(self,paramList=[]):
        print 'this is the ojService'
