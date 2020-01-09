from copy import *
a = [1,2,3,4,5]
b = a[0:3]
b.reverse()
a[0:3] = b
print(a)
