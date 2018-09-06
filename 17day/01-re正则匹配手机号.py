import re
num = input("请输入手机号")
if re.match("^1[3-9]\d{9}$",num)
	print("输入正确")
	print(num)
else:
	print("输入错误")

# ^以什么开头,   以什么结尾$,  [3-9]输入范围是3-9之间,   \d{9}九位数字
