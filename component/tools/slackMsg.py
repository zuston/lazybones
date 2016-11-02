
class slackMsg(object):
    def __init__(self):
        pass

    def sendMsg(self,channel,robotname,content,icon_emoji):
        import urllib
        import urllib2
        data = {}
        data['payload'] = '{"channel":"%s","username":"%s","text":"%s","icon_emoji":"%s"}'%(channel,robotname,content,icon_emoji)
        # data['payload'] = '{"fallback": "Required text summary of the attachment that is shown by clients that understand attachments but choose not to show them.","text": "Optional text that should appear within the attachment","pretext": "Optional text that should appear above the formatted data","color": "#36a64f","fields": [{"title": "Required Field Title","value": "Text value of the field. May contain standard message markup and must be escaped as normal. May be multi-line.","short": "false"}]}'
        url = 'https://hooks.slack.com/services/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'
        post_data = urllib.urlencode(data)
        req = urllib2.urlopen(url,post_data)
        content = req.read()
        return content

if __name__ == '__main__':
    sendm = slackMsg()
    sendm.sendMsg('#zbot','robot','first connecting',':ghost:')
