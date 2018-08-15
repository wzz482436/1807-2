class car():
	def __init__(self,color,xinghao):
		self.color=color
		self.xinghao=xinghao

	def move(self):
		print("跑")
	def music(self):
		print("啦啦啦")
	
	
k=car("红色","宇宙超级无敌吊炸天牌")
print("我是一辆特别牛逼的车,我有%s的外形,%s的型号"%(k.color,k.xinghao))
