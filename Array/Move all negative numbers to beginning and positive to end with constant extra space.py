#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 23:00
# @Author  : LI Dongdong
# @FileName: Move all negative numbers to beginning and positive to end with constant extra space.py
''''''
'''

1.要求：An array contains both positive and negative numbers in random order.
    Rearrange the array elements so that all negative numbers appear before all positive numbers.
    Input : -12, 11, -13, -5, 6, -7, 5, -3, -6
    Output :-12 -13 -5 -7 -3 -6 11 6 5
    Note :- Order of elements is not important here.
2.理解：把正数放在负数之前，进行排序
3.类型：排序题
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:None? Y One? Y repeat? Y order? N
    output: arr/arr...
    focus on time or space? space
'''

'''
idea：brute force
Method：sort function
time complex: O(NlogN)
space complex: O(N)
易错点：
'''
class sortArr:
    def sortPN(self, arr):  # put the negative front fo positive value
        arr.sort()
        return arr

x = sortArr()
print(x.sortPN([9,8,7,4,5,-1, -2, -3]))


