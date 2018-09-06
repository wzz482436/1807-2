class Car():
	def __init__(self,color):
		self.color = color

	def run(self):
		print("-------run--------")
	
class Bmw(Car):
	def __init__(self,color):
		self.count = 6
		super().__init__(color)
	def run(self):
		print("bmw -----run------")

class Benchi(Car):
	def run(self):
		print("benchi-------run-----")
	
class Bieke(Car):
	def run(self):
		print("bieke-----run-----")
		
class Factory(): #抽象类
	def create(self): #抽象方法
		pass
bmw = Bmw("红色")
print(bmw.color)
bmw.run()

benchi = Benchi("白色")
print(benchi.color)
benchi.run()

bieke = Bieke("黑色")
print(bieke.color)
bieke.run()
