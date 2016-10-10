#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'zuston'
# 监听消息queue的请求
import sys
import time
import os
sys.path.append('..')
from funtools import redisQueue as rq
from funtools import slackMsg as sm

def supervisorQueue():
    content = _getCommand()
    if content is None:
        print 'redis中无数据.....'
    else:
        # robot:oj send 12,23,54,65
        splitList = content.split(':')
        cmd = splitList[1].strip()
        execode,res = _checkCommand(cmd)
        if execode==1:
            # serviceClass,serviceFunction,serviceParam = cmd.split(' ')
            # code,e=_boundClass(serviceClass,serviceFunction,serviceParam)
            # print e
            response = '成功'
            _send2Slack([execode,response])
        else:
            print execode,res
            _send2Slack([execode,res])

def loopSupervisor():
    while True:
        supervisorQueue()
        time.sleep(1)


def _send2Slack(list=[]):
    if list[0]==1:
        msg = list[1]
    if list[0]==0:
        # TODO: 发送的格式需要改进
        msg = 'command格式:\n'
        for key in list[1]:
            for value in list[1][key]:
                msg += 'robot:'+key+' '+value+' params'+'\n'
    sendm = sm.slackMsg()
    sendm.sendMsg('#zbot','robot',msg,':ghost:')

def _boundClass(classname,func,param):
    try:
        module = __import__("service."+classname+'Service')
        service = getattr(module,classname+'Service')
        instance = getattr(service,classname+"Service")
        function = getattr(instance(),func+'Action')
        paramList = _parseParam(param)
        return function(paramList)
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
    loopSupervisor()
