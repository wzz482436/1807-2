import time
import re

def writeLog(msg):
	with open("1.txt","a") as f:
		f.write(msg)
def w1(fun):
	def inner(*args,**kwargs):
		msg  = str(fun)+str(time.ctime())+"\n"
		writeLog(msg)
		fun(*args,**kwargs)
	return inner

class Hotel():
	def __init__(self,name,phone):
		self.name = name
		self.phone = phone
		self.list = []
		self.money = 0
	@w1
	def inHome(self,person):
		person.time = int(time.time())
		person.islive = True
		self.list.append(person)
		print("入住成功")
	@w1
	def outHome(self,name):
		for person in self.list:
			if person.name == name:
				person.islive = False
				endtime = int(time.time())
				diff_money = (endtime - person.time)*10
				print("花了%.02f"%diff_money)
				self.money+=diff_money
				break
				print("离店成功")
	@w1
	def tongji(self):
		count = 0
		for person in self.list:
			if not person.islive:
				count+=1
		print("今天总入住%d人!离店%d人 收入%.02f"%(len(self.list),count,self.money))
                
class Person():
	def __init__(self,name,phone):
		self.name = name
		self.phone = phone
	def CheckPhone(self,phone):
		if re.match(r"1[3-9]\d{9}$",phone):
			self.phone = phone
		else:
			print("输入错误")
zz = Hotel("哈哈哈",16619737071)
while True:
	num = int(input("请选择功能 1:住店 2:离店 3:统计 4:退出"))
	if num == 1:
		name = input("请输入名字")
		phone = input("请输入手机号")
		wzz = Person(name,phone)
		wzz.CheckPhone(phone)
		zz.inHome(wzz)
	elif num == 2:
		name = input("请输入姓名")
		zz.outHome(name) 
	elif num == 3:
		zz.tongji()
	elif num == 4:
		exit()

