#list = [{"name":"王志洲","age":17},{"name":"洲洲","age":17}]

'''
f = open("data.data","w")
f.write(str(list))
f.close()
'''

import pprint

files=[{"name":"王志洲","age":17},{"name":"洲洲","age":17}]
s=pprint.pformat(files)

print(type(s))
print(s)
