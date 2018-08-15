class car:
	
	def eat(self):
		print("吃")
	def sleep(self):
		print("睡觉")
	def introduce(self):
		print("大家好我叫%s,我今年%d岁"%(self.name,self.age))
wzz=car()
wzz.name="洲洲"
wzz.age=17
#wzz.eat()
#wzz.sleep()
wzz.introduce()
#print(wzz.name)
#print(wzz.age)

chen=car()
chen.name="辰辰"
chen.age=18
#chen.eat()
#chen.sleep()
chen.introduce()
#print(chen.name)
#print(chen.age)
