import re
num = input("请输入手机号")
if re.match("^1[3-9]\d\d\d\d\d\d\d\d\d",num):
	print("输入正确")
	print(num)
else:
	print("输入错误")
