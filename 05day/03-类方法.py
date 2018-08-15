class Dog():
    print("哈哈哈哈哈哈")
    count = 10#类属性
    __count1 = 20#私有类属性
    def __init__(self,name):
        self.name = name#实例属性
        self.__age = 10#私有属性


    def getAge(self):
        return self.__age
   
    ''' 
    def getCount1(self):
        return Dog.count
    '''        
 
    @classmethod
    def getCount(cls):
        print("我是类方法")
        return cls.count

    @classmethod
    def getCount1(cls):
        return cls.__count1

tom = Dog("Tom")#创建实例对象
print(tom.name)
print(tom.getAge())

#print(Dog.count)#通过类访问类属性

Dog.getCount()#通过类访问类方法
#tom.getCount()#通过对象访问类方法

#print(tom.getCount1())

#print(Dog.__count1)#不能访问私有类属性
print(Dog.getCount1())#通过公有的类方法访问私有类属性

