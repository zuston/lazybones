class redisQueue(object):
    def __init__(self):
        pass

    def inQueue(self,request):
        token = request.form['token']
        team_id = request.form['team_id']
        team_domain = request.form['team_domain']
        channel_id = request.form['channel_id']
        channel_name = request.form['channel_name']
        timestamp = request.form['timestamp']
        user_id = request.form['user_id']
        user_name = request.form['user_name']
        text = request.form['text']
        trigger_word = request.form['trigger_word']
        pass

    def popQueue(self):
        pass

    def test(self):
        return 200;

if __name__ == '__main__':
    pass
