class Dog():
    __x = None 
    def __new__(cls):
        if cls.__x == None:
            cls.__x = super().__new__(cls)
            return cls.__x
        else:
            return cls.__x

dog1 = Dog()
print(id(dog1))

dog2 = Dog()
print(id(dog2))

