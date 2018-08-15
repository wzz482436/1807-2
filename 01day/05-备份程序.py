name = input("请输入备份文件名字（要有后缀名）")
f = open(name,"r")
content = f.read()

#newname = name+"备份"#密码.txt备份

position = name.rfind(".")
newname = name[:position]+"备份"+name[position:]
f1 = open(newname,"w")
f1.write(content)

f.close()
f1.close()
