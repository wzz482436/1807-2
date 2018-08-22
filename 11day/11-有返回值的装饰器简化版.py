def w1(fun):
    def inner():
        print("-----验证中-----")
        return fun()
    return inner

@w1#相当于pay = w1(pay)  语法糖
def pay():
    print("支付中")
    return "洲洲"

ret = pay()#此时装饰器已经装饰完毕
print(ret)
