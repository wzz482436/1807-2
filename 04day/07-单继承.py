class Animal():
    pass


class Cat(Animal):
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self,name):
        self.name = name


bsm = Cat("波斯猫")
print(bsm.name)

wc = Dog("旺财")
print(wc.name)
