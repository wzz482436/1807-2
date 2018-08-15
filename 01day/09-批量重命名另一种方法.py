import os
dir = input("请输入 想要 批量重命名的文件 所在文件夹的名字 ")
files= os.listdir(dir)
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"-洲洲"+i[position:]
	oldname = dir+"/"+i
	newname = dir+"/"+newname
	os.rename(oldname,newname)

