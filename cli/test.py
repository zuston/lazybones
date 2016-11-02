import sys
sys.path.append("..")

import component.commonInterface.pluginManage as pm
import component.commonInterface.pluginAct as pa


def test_GetAllPlugin():
    pluginManageInstance = pm.pluginManage()
    pluginManageInstance.getAllPlugin()

def test_act():
    instance = pa.pluginAct("newsService","get")
    print instance.act()

if __name__ == "__main__":
    test_GetAllPlugin()
    test_act()