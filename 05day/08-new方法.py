class Dog(object):
    def __init__(self):#初始化属性 得先有对象 
        self.name = "hadou"

    def __str__(self):
        return "I am dog"

    def __del__(self):
        print("dog die")

    def __new__(cls):#new方法
        return super().__new__(cls)
dog = Dog()#执行init
print(dog)#执行str方法
del dog #执行del方法    
