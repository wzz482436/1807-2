import re
import time
class binguan():
	def __init__(self):
		self.list=[]
		self.money = 0

	def ruzhu(self):
	
		d={}
		name = input("请输入姓名:")
		phone = input("请输入手机号:")
		if re.match("^1[3-9]\d{9}$",phone):
			print("验证通过")
			d["name"]=name
			d["phone"]=phone
			print(name)
			print(phone)
			self.list.append(d)
			starttime=int(time.time())
		else:
			print("请重新输入")

	def out(self,name):
		name = input("请输入姓名:")		
		for person in self.list:
			if person.name == name:
				endtime = int(time.time())
				enmoney = (endtime - starttime)*10
				print("一共花了%.02f"%enmoney)
				self.money+=enmoney
				break

	def tongji(self):
		count = 0
		for j in self.list:
			if not j.islive:
				count+=1
				print("今天总入住%d人,离店%d人"%(len(self.list),count))


bg = binguan()

while True:
	num = int(input("请选择功能 1:入住 2:离开 3:统计 4:退出"))
	if num == 1: 
		bg.ruzhu()
	elif num == 2:
		bg.out()
	elif num == 3:
		bg.tongji()
	elif num == 4:
		exit()



