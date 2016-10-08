# -*- coding:utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import sys

class mailTool(object):
    def __init__(self,mailConfig):
        self.mailAccount = mailConfig['mailAccount']
        self.mailPwd = mailConfig['mailPwd']
        self.smtpServer = mailConfig['smtpServer']
        self.popServer = mailConfig['popServer']
        self.sendAddr = mailConfig['sendAddr']
        self.subject = mailConfig['subject']
        self.suffix = 'txt'

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def setSuffix(self,suffix):
        self.suffix = suffix

    def sendMail(self,mailInfo,attchmentPath=None):
        msg = MIMEMultipart()
        msg['From'] = self._format_addr(u'<%s>' % self.mailAccount)
        msg['To'] = self._format_addr(u'<%s>' % self.sendAddr)
        msg['Subject'] = Header(u'%s'self.subject, 'utf-8').encode()
        # 发送内容
        msg.attach(MIMEText(mailInfo,'plain','utf-8'))
        if attchmentPath is not None:
            with open(attchmentPath,'rb') as file:
                mime = MIMEBase(self.suffix,self.suffix,filename='leetcode.'+self.suffix)
                mime.add_header('Content-Disposition', 'attachment', filename='leetcode.'+self.suffix)
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(file.read())
                encoders.encode_base64(mime)
                msg.attach(mime)

        server = smtplib.SMTP(self.smtpServer, 25)  # SMTP协议默认端口是25
        server.set_debuglevel(0)
        server.login(self.mailAccount, self.mailPwd)
        server.sendmail(self.mailAccount, self.sendAddr, msg.as_string())
        server.quit()


    def getMail(self):
        pass

    def testConfigPath(self):
        print self.mailAccount
        print self.mailPwd

if __name__ == '__main__':
    zmail = mailTool()
    config = {'mailAccount':'zuston@sina.cn'}
    # zmail.sendMail('你好吗,很想你','../../data/excel-file/0815.xlsx')
