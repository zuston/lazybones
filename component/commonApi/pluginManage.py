# coding:utf-8
__author__ = "zuston"

import re
import os

class pluginManage(object):
    def __init__(self,pluginService=None):
        self.pluginPath = "../service" if pluginService==None else pluginService
        self.pluginIdentify = "Service"
        self.pluginDict = {}

    '''
    return the determined of the param ---> plugin's function
    '''
    def getOnePluginAll(self,pluginName):
        if self.pluginDict.__len__()==0:
            self.getAllPlugin()
        for k,v in self.pluginDict.items():
            for kk,vv in v.items():
                if pluginName==kk:
                    return {k:{pluginName:vv}}
        return None

    def exsitPlugin(self):
        if self.pluginDict.__len__()==0:
            self.getAllPlugin()

    '''
    return all plugin name
    '''
    def getAllPlugin(self):
        for allFile in os.listdir(self.pluginPath):
            if allFile=="__init__.py" or re.match("^.*\.pyc$",allFile) is not None:
                continue

            pluginName , pluginSuffix  = allFile.split(".")

            if pluginSuffix not in self.pluginDict:
                self.pluginDict[pluginSuffix] = {}
            if pluginName not in self.pluginDict:
                self.pluginDict[pluginSuffix][pluginName] = []
            if pluginSuffix=="py":
                import sys
                sys.path.append("..")
                module = __import__("service."+pluginName)
                service = getattr(module,pluginName)
                instance = getattr(service,pluginName)
                for function in dir(instance()):
                    if re.match("^.*Action$",function) is not None:
                        self.pluginDict[pluginSuffix][pluginName].append(function.split("A")[0])
            else:
                self.pluginDict[pluginSuffix][pluginName] = []

        return self.pluginDict


