#打印菜单
cards = []#定义空列表
def print_menu():
	print("学生信息管理系统v2.0".center(30,"*"))
	print("1:新增学生".center(30," "))
	print("2:查询学生".center(30," "))
	print("3:修改学生".center(30," "))
	print("4:删除学生".center(30," "))
	print("5:全部学生".center(30," "))
	print("6:退出系统".center(30," "))

#保存名片

def save():
	with open("card.data","w") as f:
		f.write(str(cards))

#读名片

def readCard():
	global cards
	try:
		with open("card.data") as f:
			cards = eval(f.read())
	except FileNotFoundError:
		pass

#分发功能模块
def input_fun():
	while True:
		fun_num = int(input("请选择功能"))
		if fun_num == 1:
			add_card()
		elif fun_num == 2:
			find_card()
		elif fun_num == 3:
			update_card()
		elif fun_num == 4:
			del_card()
		elif fun_num == 5:
			all_card()
		else:
			break
#新增名片
def add_card():
	card = {}
	name = input("请输入名字")
	sex = input("请输入性别")
	age = int(input("请输入年龄"))
	phone = int(input("请输入手机号"))
	card["name"] = name
	card["sex"] = sex
	card["age"] = age
	card["phone"] = phone
	cards.append(card)
	print("添加成功")
	save()

def find_card():
	name = input("请输入要查的名字")
	flag = 0 #假设没有
	for temp in cards:
		if name == temp["name"]:
			print("名字:%s\n性别:%s\n年龄:%d\n电话:%d\n"%(temp["name"],temp["sex"],temp["age"],temp["phone"]))
			flag = 1
	if flag == 0:
		print("查无此人")
#修改名片
def update_card():
	name = input("请输入要修改的名字")
	flag = 0 #默认没有
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			print("1:修改名字")
			print("2:修改性别")
			print("3:修改年龄")
			print("4:修改手机")
			update_num = int(input("请输入要修改的选项"))
			if update_num == 1:
				new_name = input("请输入新的名字")	
				temp["name"] = new_name
			elif update_num == 2:
				new_sex = input("请输入新的性别")
				temp["sex"] = new_sex
			elif update_num == 3:
				new_age = int(input("请输入新的年龄"))
				temp["age"] = new_age
			elif update_num == 4:
				new_phone = int(input("请输入新的手机号"))
				temp["phone"] = new_phone
			else:
				print("input is error")
	if flag == 0:
		print("没有此人")
#删除名片
def del_card():
	name = input("请选择删除的名字")
	flag = 0 #假设没有
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			cards.remove(temp)
	if flag == 0:
		print("没有此人")
#打印名片
def all_card():
	print("名字".center(8," "),end=" ")
	print("性别".center(8," "),end=" ")
	print("年龄".center(8," "),end=" ")
	print("手机号".center(8," "))

	for temp in cards:
		print(temp["name"].center(8," "),end = " ")
		print(temp["sex"].center(8," "),end = " ")
		print(temp["age"].center(8," "),end = " ")
		print(str(temp["phone"]).center(13," "))
		#print("%s\t%s\t%d\t%d"%(temp["name"],temp["sex"],temp["age"],temp["phone"]))		



readCard()
print_menu()
input_fun()
