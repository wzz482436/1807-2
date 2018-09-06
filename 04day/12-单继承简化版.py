class animal():
	def __init__(self,name):
		self.name=name

	def run(self):
		print("狗在跑")

class dog(animal):
	pass


wc=dog("旺财")
print(wc.name)
wc.run()
