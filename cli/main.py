#coding:utf-8

import sys
sys.path.append("..")

import component.commonApi.pluginAct as pa
import component.commonApi.pluginManage as pm
import component.tools.redisQueue as rq
import component.tools.slackMsg as sm
import time
import logging

def __getCommand():
    redisInstance = rq.redisQueue("zqueue")
    queueContent = redisInstance.popQueue()
    return queueContent

def __removeTrigger(queueContent):
    commandString = queueContent.split(":")[1].strip()
    commandList = commandString.split(" ")
    return commandList


def __getAllCommand():
    allCommand = pm.pluginManage()
    return allCommand.getAllPlugin()

def __getOneCommandAll(pluginName):
    return pm.pluginManage().getOnePluginAll(pluginName)



def __controller(commandList):
    commandListLength = len(commandList)
    if commandListLength==1:
        if __getOneCommandAll(commandList[0])==None:
            return __getAllCommand()
        else:
            return __getOneCommandAll(commandList[0])
    if commandListLength>3:
        return __getAllCommand()

    pluginName = commandList[0]
    pluginFunction = commandList[1]
    pluginParam = commandList[2] if commandListLength==3 else None

    if __getOneCommandAll(pluginName)==None:
        return __getAllCommand()

    for language,dictionary in __getOneCommandAll(pluginName).items():
        if pluginFunction not in dictionary[pluginName] and len(dictionary[pluginName])!=0:
            return __getOneCommandAll(pluginName)

    pluginActInstance = pa.pluginAct(pluginName,pluginFunction,pluginParam)
    actRes = pluginActInstance.act()
    if actRes==None:
        return __getAllCommand()
    else:
        return actRes


def __sendAuto(taskInfo):
    '''
    taskInfo is dict
    example:
    {'py': {'newsService': ['get', 'put']}}
    {1: '[0,"weatherService function:gtAction not exist"]'}
    :param taskInfo:
    :return:
    '''
    if 0 in taskInfo.keys() or 1 in taskInfo.keys():
        return __sendSlack(taskInfo,1)
    else:
        return __sendSlack(taskInfo,0)

def __sendSlack(taskInfo,infoType):
    slackInstance = sm.slackMsg()
    if infoType==1:
        info = "有执行结果"
    if infoType==0:
        info = "提示信息"
    slackInstance.sendMsg('#zbot', 'robot', info, ':ghost:')

def loop():
    while(True):
        queueContent = __getCommand()
        if queueContent==None:
            time.sleep(1)
            continue
        commandList = __removeTrigger(queueContent)
        taskInfo = __controller(commandList)
        __sendAuto(taskInfo)

def test():
    print __sendAuto(__controller(["newsService","gt"]))
    print __sendAuto(__controller(["weatherService","get","上海"]))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/service.log',
                        filemode='w')
    loop()










