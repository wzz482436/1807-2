#coding=utf-8
import os
import time

# 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
pid = os.fork()
if pid == 0:
    print('哈哈1')
else:
    print('哈哈2')

pid = os.fork()
if pid == 0:
    print('哈哈3')
else:
    print('哈哈4')

time.sleep(1)
