# -*- coding:utf-8 -*-

import sys
sys.path.append('..')
import component.tools.mailTool as mt
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
        return {1:"the mail is flying to her!"}
