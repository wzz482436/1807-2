class baba():
    __x = None 
    __y = False
    def __init__(self,name):
        if baba.__y == False:
            baba.name = name 
            baba.__y = True

    def __new__(cls,name):#重写
        if cls.__x == None:
            cls.__x = super().__new__(cls)
            return cls.__x
        else:
            return cls.__x

wzz = baba("洲洲")
print(id(wzz))
print(wzz.name)

wzz2 = baba("啦啦啦")
print(id(wzz2))
print(wzz.name)





