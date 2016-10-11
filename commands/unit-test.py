#coding:utf-8
import supervisorQueue as sq

def testCommand():
    code,res=sq._checkCommand('news kiasd')
    if code:
        print '校验参数，执行命令'
    else:
        print res

def testCommand2Service():
    string = 'robot:oj send 好的,45,12'
    splitList = string.split(':')
    print splitList[1].split(' ')
    servicename = splitList[1].split(" ")[0]
    print servicename
    module = __import__("service."+servicename+'Service')
    ser = getattr(module,servicename+'Service')
    instance = getattr(ser,servicename+'Service')
    print dir(instance())
    exit(1)
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

def listType():
    list = ['jello',"jei"]
    if type(list)==list:
        print 'i am list'
    else:
        print 'i not list'
if __name__ == '__main__':
    # testCommand2Service()
    # sq.loopSupervisor()
    listType()
