import os
dir = input("请输入")
x=os.listdir(dir)
os.chdir(dir)
print(os.getcwd())
for i in x:
	y= i.rfind(".")
	newname=i[:y]+"hh"+i[y:]
	os.rename(i,newname)
