#!/bin/bash

# sudo pip install redis
# sudo pip install flask

if [ ! -n "$1" ]; then
  echo 'please enter the param,the command format is:'
  echo '=============================================='
  echo './make.sh start'
  echo './make.sh stop'
  echo './make.sh install'
  echo './make.sh restart'
  echo '=============================================='
  echo 'if the permission deny ,please execute:'
  echo 'chmod +x ./make.sh'
else
  if [ "$1" = "start" ]; then
    nohup python steup.py &> /dev/null &
    cd ./commands
    nohup python supervisorQueue.py &> /dev/null &
  elif [ "$1" = "stop" ]; then
    killall python
  elif [ "$1" = "install" ]; then
    sudo pip install flask
    sudo pip install redis
  elif [ "$1" = "restart" ]; then
    #statements
    ./make.sh stop
    ./make.sh start
  else
    echo 'please enter the param,the command format is:'
    echo '=============================================='
    echo './make.sh start'
    echo './make.sh stop'
    echo './make.sh install'
    echo '=============================================='
    echo 'if the permission deny ,please execute:'
    echo 'chmod +x ./make.sh'
  fi
fi
