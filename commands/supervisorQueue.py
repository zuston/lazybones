#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'zuston'
# 监听消息queue的请求
import sys
import time
sys.path.append('..')
from funtools import redisQueue as rq

def supervisorQueue():
    rd = rq.redisQueue('zqueue')
    print rd.popQueue()


def loopSupervisor():
    while True:
        supervisorQueue()
        time.sleep(5)


if __name__ == '__main__':
    loopSupervisor()
