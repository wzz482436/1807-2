import os
class FileMan():
    def delFile(self):
        dir = input("请输入批量重命名的文件夹名字")
        files = os.listdir(dir)#列表
        #os.chdir(dir)
        #print(os.getcwd())
        for i in files:
            position = i.rfind(".")
            newname = i[:position]+"-阿里"+i[position:]
            oldname = dir+"/"+i#movie/吃鸡.py
            newname = dir+"/"+newname
            os.rename(oldname,newname)

fm = FileMan()
fm.delFile()
