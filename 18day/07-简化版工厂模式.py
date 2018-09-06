class BmwStore(object):
	def order(self,type):
		if type == 0:
			return Bmw730()
		elif type == 1:
			return Bmwx5()
				

class Car(object):
	def move(self):
		print("在移动")

	def music(self):
		print("播放音乐")	


class Bmw730(Car):
	pass


class Bmwx5(Car):
	pass



if __name__ == '__main__':
	store = BmwStore()
	bmwx5 = store.order(1)
	bmwx5.move()
	bmwx5.music()	
