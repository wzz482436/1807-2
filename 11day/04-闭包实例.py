def wzz(a,b):
	def zz(x):
		return a*x+b
	return zz

#y=2x+3
zz=wzz(2,3)
print(zz(5))
print(zz(6))
print(zz(7))

def wzz1(a,b,x):
	return a*x+b

print(wzz1(2,3,5))
print(wzz1(2,3,6))
print(wzz1(2,3,7))
