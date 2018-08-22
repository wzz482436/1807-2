class DateTool():

    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d
    
    def print_show(self):
        print("今年是%s年%s月%s日"%(self.y,self.m,self.d))

    @classmethod
    def del_date(cls,date):
        '''
        y,m,d = str.split("-")
        return y,m,d
        '''
        ''' 
        y,m,d = str.split("-")
        return cls(y,m,d)   #相当于DateTool(y,m,d)
        '''
        y,m,d = str.split("-")
        cls(y,m,d).print_show() 
'''
str1 ="2018-8-10"
str2 = "2018-08-02"
st4 = "2018-08-2"
'''

str = "2018-08-10"
y,m,d = str.split("-")
dt = DateTool(y,m,d)
dt.print_show()

'''
str = "2018-08-10"
y,m,d = DateTool.del_date(str)
dt = DateTool(y,m,d)
dt.print_show()
'''

'''
str = "2018-08-10"
dt = DateTool.del_date(str)
dt.print_show()
'''
'''
str = "2018-08-10"
DateTool.del_date(str)
'''
