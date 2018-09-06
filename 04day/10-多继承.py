class A():
    def __init__(self):
        self.name = "辰辰"
        self.age = 20

    def show(self):
        print("洲洲")
class B():
    def show1(self):
        print("哈哈哈")


class C(A,B):
    pass


c = C()
print(c.name)
print(c.age)
c.show()
c.show1()
print(C.__mro__)
