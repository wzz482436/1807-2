import re
ret = input("请输入")
if re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",ret):
	print(ret)
	print("输入正确")
