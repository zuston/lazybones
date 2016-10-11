#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'zuston'
# 监听消息queue的请求
import sys
import time
import os
import logging
sys.path.append('..')
from funtools import redisQueue as rq
from funtools import slackMsg as sm

def supervisorQueue():

    content = _getCommand()
    if content is None:
        # logging.info('empty')
        pass
    else:
        # robot:oj send 12,23,54,65
        splitList = content.split(':')
        cmd = splitList[1].strip()
        execode,res = _checkCommand(cmd)
        logMsg = ''
        if execode==1:
            # TODO: 参数解析的话针对有的service无参数，有的有参数，外部无法获取类方法的参数集合，需要改进
            if len(cmd.split(' '))==3:
                serviceClass,serviceFunction,serviceParam = cmd.split(' ')
                code,e=_boundClass(serviceClass,serviceFunction,serviceParam)
            else:
                serviceClass,serviceFunction = cmd.split(' ')
                code,e=_boundClass(serviceClass,serviceFunction)
            if code==1:
                logMsg += 'service act successfully'
                response='service act successfully'
            else:
                logMsg+='service has error'
                response = res
            _send2Slack([execode,response])
        else:
            logMsg += 'command has problems'
            _send2Slack([execode,res])
        logging.info('\ncmd:[%s] %s\n========================'%(content,logMsg))


def loopSupervisor():
    while True:
        supervisorQueue()
        time.sleep(1)


def _send2Slack(lst=[]):
    if lst[0]==1:
        msg = lst[1]
    if lst[0]==0:
        if type(lst) == list:
            # TODO: 发送的格式需要改进
            msg = '---command格式---\n'
            for key in lst[1]:
                for value in lst[1][key]:
                    msg += 'robot:'+key+' '+value+' params'+'\n'
            msg += '---------------\n'
        else:
            msg = lst[1]
    print msg
    sendm = sm.slackMsg()
    sendm.sendMsg('#zbot','robot',msg,':ghost:')

# param参数为string,暂时根据具体的方法内部来进行解析
def _boundClass(classname,func,param=None):
    try:
        module = __import__("service."+classname+'Service')
        service = getattr(module,classname+'Service')
        instance = getattr(service,classname+"Service")
        function = getattr(instance(),func+'Action')
        return function() if param is None else function(param)
    except Exception,e:
        return [0,e]


def _parseParam(param):
    paramList = []
    for oneparam in param.split(','):
        try:
            changeNum = int(oneparam)
            paramList.append(changeNum)
        except ValueError:
            paramList.append(oneparam)
    return paramList

# 获取service下面的命令列表
# TODO: 参数未获取，需要获取
def _commandList():
    serviceName = {}
    import re
    for filename in os.listdir('../service'):
        if filename!="__init__.py" and re.match('^.*\.pyc$',filename) is None:
            serviceName[filename.split('S')[0]] = []
            module = __import__("service."+filename.split('.')[0])
            ser = getattr(module,filename.split('.')[0])
            instance = getattr(ser,filename.split('.')[0])
            for classAction in dir(instance()):
                if re.match("^__.*__$",classAction) is None and re.match("^.*Action$",classAction) is not None:
                    # print classAction
                    serviceName[filename.split('S')[0]].append(classAction.split('A')[0])
    # {'oj': ['send', 'test']}
    # {'news': ['get'], 'oj': ['test']}
    # 此为 robot:oj send param
    # 此为 robot:oj test param
    return serviceName

def _checkCommand(cmd):
    if cmd=='':
        return [0,_commandList()]
    paramCount = len(cmd.split(' '))
    if _commandList().has_key(cmd.split(' ')[0]):
        dictCommand = _commandList()
        if paramCount==1:
            return [0,{cmd.split(' ')[0]:dictCommand[cmd.split(' ')[0]]}]
        else:
            if cmd.split(' ')[1] in dictCommand[cmd.split(' ')[0]]:
                return [1,'ok']
            else:
                return [0,{cmd.split(' ')[0]:dictCommand[cmd.split(' ')[0]]}]
    else:
        return [0,_commandList()]

def _getCommand():
    rd = rq.redisQueue('zqueue')
    content = rd.popQueue()
    return content

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/service.log',
                        filemode='w')
    loopSupervisor()
