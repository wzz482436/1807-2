import re
'''
age = "我今年12岁"
print(re.sub(r"(\d+)",lambda x: str(int(x.group())+5),age))
'''
#使用函数格式
def add(x):
	num = int(x.group())+5
	return str(num)

age = "我今年12岁"
print(re.sub(r"(\d+)",add,age))


