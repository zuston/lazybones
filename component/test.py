#coding:utf-8
import commonInterface.pluginManage as pm
import commonInterface.pluginAct as pa
import json

def test_GetAllPlugin():
    instance = pm.pluginManage()
    print instance.getAllPlugin()

def test_GetOnePluginAll():
    instance = pm.pluginManage()
    print instance.getOnePluginAll("newsService")
    print instance.getOnePluginAll("heloService")


def test_act():
    instance = pa.pluginAct("weatherService","get","上海")
    print instance.act()


def testJson():
    string = '[1,"["\u4e0a\u6d77\u5f53\u524d\u5929\u6c14:\u6e29\u5ea6:17 ~ 10\u2103,\u6674,\u98ce\u529b:\u5317\u98ce\u5fae\u98ce."]"]'
    print json.loads(string)

if __name__ == "__main__":
    test_GetAllPlugin()
    test_GetOnePluginAll()
    print "------"
    test_act()
    print "========="
    testJson()