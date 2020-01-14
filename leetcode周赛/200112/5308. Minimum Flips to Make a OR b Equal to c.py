#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 11:45
# @Author  : LI Dongdong
# @FileName: 5308. Minimum Flips to Make a OR b Equal to c.py
''''''
'''
题目分析
1.要求：Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
a -> 0010 b ->0110 c ->0101
a -> 0001 b -> 0100 c->0101
2.理解：
3.类型：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：
方法：
边界条件：
time complex: 
space complex: 
易错点：
'''


# class Solution:
#     def difNum(self, numb1, numb2): #二进制中不一样的个数
#         dif = numb1^numb2
#         res = 0
#         for elem in bin(dif)[2:]:
#             if elem == '1':
#                 res += 1
#         return res
#
#     def comNum(self, numb1, numb2): # 二进制中一样的个数
#         com = numb1^numb2
#         res = 0
#         for elem in bin(com)[2:]:
#             if elem == '0':
#                 res += 1
#         return res
#
#     def minFlips(self, a: int, b: int, c: int) -> int:
#         difAC = self.difNum(a, c)
#         difBC = self.difNum(b, c)
#         difAB = self.difNum(a & b, c) # a与b的交集，与c的相同个数
#         return difAC + difBC - difAB
#
# x = Solution()
# print(x.minFlips(2, 6, 5))
# print(2|6)


'O(32)'

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            x, y, z = (a >> i) & 3, (b >> i) & 1, (c >> i) & 1
            if z==0 and (x+y) >= 1:
                res += (x+y)
            elif z==1 and (x+y) == 0:
                res += 1
        return res

x = Solution()
print(x.minFlips(2, 6, 5))