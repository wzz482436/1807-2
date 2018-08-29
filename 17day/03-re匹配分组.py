import re
x=input("请输入")
if re.match(r"<(\w+)><(\w+)>.+</\2></\1>",x): # <x><y>洲洲</y></x> 这种格式
	print("输入正确")
	print(x)
else:
	print("输入有误")

