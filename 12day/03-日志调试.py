import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print(final)

#调试方法

# 《1 显示代码》
# l---->能够显示当前调试过程中的代码，其实l表示list列出的意思
  #如下，途中，-> 指向的地方表示要将要执行的位置
  # 2      a = "aaa"
  # 3      pdb.set_trace()
  # 4      b = "bbb"
  # 5      c = "ccc"
  # 6      pdb.set_trace()
  # 7  ->    final = a + b + c
  # 8      print final

# 《2 执行下一行代码》
# n---->能够向下执行一行代码，然后停止运行等待继续调试 n表示next的意思

# 《3 查看变量的值》
# p---->能够查看变量的值，p表示prit打印输出的意思
    #例如：
    # p name 表示查看变量name的值
