import re
x=input("请输入邮箱地址")
if re.match(r"\w{4,20}@qq.com$",x):
	print("验证通过")
	print(x)
else:
	print("输入错误")
