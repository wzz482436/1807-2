class car():
	def __init__(self):
		self.color="红色"
		self.xinghao="超级无敌吊炸天"

	def move(self):
		print("路边车在跑")
	def music(self):
		print("车厢内放着啦啦啦")

	
	
k=car()
k.move()
k.music()
print("那是一辆特别牛逼的车,有%s的外形,%s的型号"%(k.color,k.xinghao))
