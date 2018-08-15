class Dog():
    print("哈哈哈哈哈哈")
    def __init__(self,name):
        self.name = name#实例属性
        self.__age = 10


    def getAge(self):
        return self.__age




'''
tom = Dog("Tom")#创建实例对象
print(tom.name)
print(tom.getAge())
'''
