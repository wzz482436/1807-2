class Dog():
    def __init__(self):
        self.name = ""
        self.age = 0
    
    def sleep(self):
        print("sleep")

    def setAge(self,age):
        if age > 15 or age < 1:
            print("年龄不符合")
        else:
            self.age = age

    def getAge(self):
        return self.age


hsq = Dog()
hsq.age = 100
print(hsq.age)#以前获取
#hsq.setAge(100)
#print(hsq.getAge())#现在获取
