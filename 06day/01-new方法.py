class Dog(object):
    def __init__(self):
        self.name = "tom"

    def __str__(self):
        return "I am a dog"
    
    def __del__(self):
        print("I die")

    def __new__(cls):
        return super().__new__(cls)
  

dog = Dog()#创建实例对象 
print(dog)

