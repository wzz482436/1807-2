class Dog():
    def __init__(self):
        self.name = ""
        self.__age = 0#私有属性
    
    def sleep(self):
        print("sleep")

    def setAge(self,age):
        if age > 15 or age < 1:
            print("年龄不符合")
        else:
            self.__age = age

    def getAge(self):#公有方法
        return self.__age


hsq = Dog()
#print(hsq.__age)#不能直接获取了
#print(hsq.getAge())#必须通过共有方法获取

#hsq.__age = 100#就是一个普通属性
hsq.setAge(10)
print(hsq.getAge())

