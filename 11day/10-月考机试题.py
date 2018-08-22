import time
list = []
money = 0
def zhu():
	l={}
	name = input(" 请输入姓名:")
	while True:
		card = input(" 请输入身份证号:")
		if len(card) == 18:
			age = 2018-int(card[6:10])

			if age >= 18:
				print("验证通过")
				l["name"] = name
				l["card"] = card
				l["starttime"] = int(time.time())
				print(l)
				list.append(l)
				

			else:
				print(" 抱歉,本店仅支持成年人入宿,对您带来的不便还行谅解,请您离开")
				return

			break
		else:
			print(" 输入错误,请重新输入 ")
			continue

	

def tui():
	global money
	name = input(" 请输入离店人的姓名")
	for i in list:
		if name == i["name"]:
			endtime = int(time.time())
			money += (endtime- i["starttime"])*10
			list.remove(i)
			print(" 退店成功 ")
			print("一共消费%.02f元钱"%(money))
			break
			

def tongji():
	for i in list:
		print("总入住人数为%d人"%(l.count("name")))
		



def menu():
	print (" 欢迎来到志洲大宾馆 ".center(30,"*"))
	while True:

		time.sleep(1)
		print("1: 住宿 ")
		print("2: 退房 ")
		print("3: 统计 ")
		print("4: 退出系统 ")
		num = int(input("请选择: "))
		if num == 1:
			zhu()
		elif num == 2:
			tui()
		elif num == 3:
			tongji()
		elif num == 4:
			return

menu()
