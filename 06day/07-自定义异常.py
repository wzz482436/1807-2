class showError(Exception):
    def __init__(self,len):
        self.len = len
        self.x = 5#至少需要5

name = input("请输入名字")
try:
    if len(name) < 5:
        raise showError(len(name))
except showError as ret:
    print("至少需要%d位,传的值是%d"%(ret.x,ret.len))
'''
用类的方式，做一个假如输入老王就报错的程序
'''
