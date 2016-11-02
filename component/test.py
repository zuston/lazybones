#coding:utf-8
import commonApi.pluginManage as pm
import commonApi.pluginAct as pa


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

if __name__ == "__main__":
    test_GetAllPlugin()
    test_GetOnePluginAll()
    print "------"
    test_act()