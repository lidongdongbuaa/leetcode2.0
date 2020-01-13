from copy import *
a = bin(5)
b = bin(104)
print(a)
print(b)


def get_binary(num):
    '''
    得到一个整数的二进制表示列表
    '''
    binary=[]
    while num!=0:
        binary.append(str(num//2))
        num/=2
    return binary

print(get_binary(4))