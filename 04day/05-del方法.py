class Dog():
    def __init__(self):
        self.name = "二哈"
        print("init")
   
    def __str__(self):
        return "我是str方法"

    def __del__(self):
        print("我del")#当一个对象没有任何引用指向它的时候会执行

dog = Dog()#执行init方法
print(dog)#执行str方法
dog1 = dog
print(id(dog))
print(id(dog1))
del dog
del dog1
print("哈哈")

    
