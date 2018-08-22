def w(type):
    def w1(fun):
        def inner():
            if type == 1:
                print("验证1")
            elif type == 2:
                print("验证2")
            fun()
        return inner
    return w1

@w(1)#@w1
def check_login():
    print("登录")
 
check_login()   

@w(2)
def check_login1():
    print("登录1")
 
check_login1()   
