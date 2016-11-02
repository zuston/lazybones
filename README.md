# lazybones
## 原理概述
用了一下slack的[incoming](https://api.slack.com/incoming-webhooks)和[outgoing](https://api.slack.com/outgoing-webhooks)的api.<br>
具体流程是服务器起一个进程监听发送过来的请求，从而响应接收request，我是将请求放入redis中，然后另外一个进程监听redis中的数据是否存在，有的话就根据其内容来执行任务，也就是我所谓的服务
## 开发服务插件
举个🌰 . 我在slack端发送特定信息 robot:oj send love,you,zhu  <br>
解析的时候是刨除robot:这个trigger的文本，那实际上是oj send love,you,zhu这些来解析的。
这里我定义oj则对应service文件夹下的ojService.py的ojService这个类，send则是类下的sendAction这个方法，最后则是参数.这里采用的反射的机制来实现。<br>
但是由于动态语言的关系，参数的预先判断无法实现。所以代码写的不优雅。
<br>开发一个服务的话，其实只要在service下面新建一个nameService然后创建同名的类，然后就创建以Action为后缀的方法就行了。后期这里可以用命令行来实现服务的基本文本创建。
##部署
记得修改 funtools 里面的slackMsg.py里面的配置<br>
记得安装redis,ubuntu(sudo apt-get install redis)mac(brew install redis)<br>
git clone git@github.com:zuston/lazybones.git<br>
cd lazybones<br>
./make.sh install<br>
./make.sh start<br>

- [ ] shell命令实现service的文本创建
- [ ] 实现php语言开发的服务的无缝连接
- [ ] slack配置抽离出来
