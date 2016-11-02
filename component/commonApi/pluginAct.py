# coding:utf-8

__author__ = "zuston"

import os
import sys

class pluginAct(object):
    def __init__(self,pluginName,pluginFunction,pluginParams=None):
        self.pluginName = pluginName
        self.pluginFunciton = pluginFunction+"Action"
        self.pluginParams = pluginParams
        self.pluginPath = "../service"
        self.pluginFolder = "service"
        self._getSuffix()

    def _getSuffix(self):
        self.pluginSuffix = None
        for filename in os.listdir(self.pluginPath):
            if self.pluginName==filename.split(".")[0] and filename.split(".")[1]!="pyc":
                self.pluginSuffix = filename.split(".")[1]
        return self.pluginSuffix

    def bindAct(self):
        import sys
        sys.path.append("..")
        module = __import__(self.pluginFolder+"."+self.pluginName)
        instance = getattr(getattr(module,self.pluginName),self.pluginName)
        func = getattr(instance(),self.pluginFunciton)
        try:
            returnRes = func() if self.pluginParams==None else func(self.pluginParams)
            res = {1:returnRes}
        except:
            res = {0:"param error"}

        return res

    def cliAct(self):
        import commands
        import json
        path = self.pluginPath+"/"+self.pluginName+"."+self.pluginSuffix
        if self.pluginParams==None:
            paramList = ""
        else:
            paramList = self.pluginParams
        status,output = commands.getstatusoutput(self.pluginSuffix+" "+
                                                 path+" "+self.pluginFunciton+" "+
                                                 paramList)
        if status!=0:
            return {0:"参数错误"}
        else:
            return {1:output}


    def act(self):
        if self.pluginSuffix==None:
            return None

        if self.pluginSuffix=="py":
            return self.bindAct()
        else:
            return self.cliAct()

