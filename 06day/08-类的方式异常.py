class ShowError(Exception):
	def __init__(self,name):
		self.name = name


class InputManger():
	def my_input(self):
		self.name = input("请输入名字")
		try:
			if self.name == "老王":
				raise ShowError(self.name)
		except ShowError as ret:
			print("%s有毒,请不要输入"%ret.name)

im = InputManger()
im.my_input()
