import re
x=input("请输入邮箱地址")
if re.match(r"[0-9,a-z,A-Z]{4,20}@(qq|126|163).com$",x): #|代表或者的意思,要么是qq要么126要么163,只要满足其中之一就可以

#if re.match(r"\w{4,20}@(qq|126|163).com$",x): 

	print("验证通过")
	print(x)
else:
	print("输入错误")
