
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 21:27
# @Author  : LI Dongdong
# @FileName: 经典例子.py

#斐波那契数列
class X:
    def list_num(self,n):
        if n == 1 or n == 2:
            return 1

        return self.list_num(n-1) + self.list_num(n-2)


#汉诺塔
class X:
    def hanno(self,n, x, y, z):
        if n == 1:
            print(x, '->', z)
            return
        else:
            self.hanno(n-1,x,z,y)#将前n-1个盘子从x移动到y上
            self.hanno(1,x,y,z) #将最后一个盘子从x移动到z上
            self.hanno(n-1,y,x,z) #将y上n-1个盘子移动到z上

x= X()
print(x.hanno(7,'x','y','z'))