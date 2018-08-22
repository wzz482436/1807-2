import os
class FileMan():
    def delFile(self):
        dir = input("请输入批量重命名的文件夹名字")
        files = os.listdir(dir)#列表
        #os.chdir(dir)
        #print(os.getcwd())
        for i in files:
            position = i.rfind(".") #查找内容
            newname = i[:position]+"-baby"+i[position:] #在查找的内容前面加上-baby
            oldname = dir+"/"+ i #movie/吃鸡.py
            newname = dir+"/"+newname
            os.rename(oldname,newname)

fm = FileMan()
fm.delFile()
