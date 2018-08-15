class Animal():
    def eat(self):
        print("吃")



class Dog(Animal):
    def eat(self):
        print("吃狗粮")



class Cat(Animal):
    def eat(self):
        print("猫吃鱼")


def showtel(animal):
    animal.eat()

dog = Dog()
showtel(dog)

cat = Cat()
showtel(cat)


