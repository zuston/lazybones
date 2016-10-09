#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'zuston'
# 监听消息queue的请求
import sys
import time
sys.path.append('..')
from funtools import redisQueue as rq
from funtools import slackMsg as sm

def supervisorQueue():
    rd = rq.redisQueue('zqueue')
    content = rd.popQueue()
    if content is None:
        print 'redis中无数据.....'
    else:
        # robot:oj send 12,23,54,65
        splitList = content.split(':')
        cmd = splitList[1].strip().split(' ')
        cmdLen = len(cmd)
        if cmdLen==0:
            e='命令缺少执行参数'
            # TODO: 发送错误信息，-h的命令
        if cmdLen==1:
            e='缺少action'
            # TODO: 提示service下的action动作
        if cmdLen==2:
            e='待查'
        if cmdLen==3:
            serviceClass,serviceFunction,serviceParam = cmd
            code,e=_boundClass(serviceClass,serviceFunction,serviceParam)
        if cmdLen>3:
            e='参数过多,出错'
            # TODO:
        send2Slack(e)

def send2Slack(msg):
    sendm = sm.slackMsg()
    sendm.sendMsg('#zbot','robot',msg,':ghost:')

def _boundClass(classname,func,param):
    try:
        module = __import__("service."+classname+'Service')
        service = getattr(module,classname+'Service')
        instance = getattr(service,classname+"Service")
        function = getattr(instance(),func)
        paramList = _parseParam(param)
        return function(paramList)
    except Exception,e:
        # TODO: 提醒
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

def loopSupervisor():
    while True:
        supervisorQueue()
        time.sleep(1)

def test_split():
    string = 'robot:oj send 好的,45,12'
    splitList = string.split(':')
    print splitList[1].split(' ')
    servicename = splitList[1].split(" ")[0]
    print servicename
    module = __import__("service."+servicename+'Service')
    ser = getattr(module,servicename+'Service')
    instance = getattr(ser,servicename+'Service')
    func = getattr(instance(),'test')
    func()
    param = splitList[1].split(" ")[2]
    print param.split(',')
    paramList = []
    for oneparam in param.split(','):
        try:
            changeNum = int(oneparam)
            print changeNum
            paramList.append(changeNum)
        except ValueError:
            print '字符串'+oneparam
            paramList.append(oneparam)
    print paramList

if __name__ == '__main__':
    # test_split()
    loopSupervisor()
