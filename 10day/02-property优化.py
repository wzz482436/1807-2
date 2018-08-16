class wzz():
	def __init__(self):
		self.__age=17

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,new):
		self.__age=new

zz=wzz()
zz.age=18
print(zz.age)
