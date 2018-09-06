import re
x = input("请输入一个数字")
if re.match("[1-9]?\d$|100",x):
	print("验证通过")
	print(x)
else:
	print("验证失败")
