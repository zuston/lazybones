#coding:utf-8
import json
class slackMsg(object):
    def __init__(self):
        pass

    def sendMsg(self,channel,robotname,content,icon_emoji,infoType,queueContent):
        import urllib
        import urllib2
        data = {}
        fieldsList = []
        if infoType==0:
        #     提示信息
            contentDict = content
            for language,dict in contentDict.items():
                for k,v in dict.items():
                    for one in v:
                        fieldsList.append({"title":"刚执行的命令"+queueContent,"value":k+" "+one+" params","short":"true"})
                        # fieldsList.append({"title":"","value":"","short":"true"})
            noticeInfo = "command help"
            color = '#FF0000'
        else:
            fieldsList.append({"title":"刚执行的命令"+queueContent,"value":content,"short":"true"})
            noticeInfo = "command feedback"
            color = "#4EEE94"
        infoDict = {
            "icon_emoji":icon_emoji,
            "username":robotname,
            "channel":channel,
            "fallback": "来自遥远火星的lazybones提示",
            "color": color,
            "pretext": noticeInfo,
            "author_name": "zuston",
            "author_link": "http://zuston.github.io/",
            "author_icon": "https://avatars1.githubusercontent.com/u/8609142?v=3&s=466",
            "title": "lazybones提示",
            "title_link": "https://github.com/zuston/lazybones",
            "fields": fieldsList,
            "footer": "lazybones API",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png"
        }
        data['payload'] = json.dumps(infoDict)
        url = 'https://hooks.slack.com/services/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'
        post_data = urllib.urlencode(data)
        req = urllib2.urlopen(url,post_data)
        content = req.read()
        return content


