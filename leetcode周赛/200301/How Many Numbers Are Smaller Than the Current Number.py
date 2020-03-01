#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 11:32
# @Author  : LI Dongdong
# @FileName: How Many Numbers Are Smaller Than the Current Number.py
''''''
'''
题目分析
1.要求：
2.理解：in a arr, count how many elem in this list < list[i], output
3.类型：array
4.确认输入输出及边界条件：
    input: list, length? 2<= <= 500; value range? 0<= <= 100, repeated? Y, order? N
    output: list[int]
    corner case: None? N, only One? N
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. Brute force
    Method:
        1. scan elem in list one by one
            scan other elem in list
                count the numb of smaller
            save count in res
        2. return res
    time complexity O(N**2), space O(N)
易错点：
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums):  # return list[int]
        res = []
        for i in range(len(nums)):
            tmp = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    tmp += 1
            for k in range(i + 1, len(nums)):
                if nums[k] < nums[i]:
                    tmp += 1
            res.append(tmp)
        return res

'''
test case
nums = [6,5,4,8]
loop 1:
    i = 0
    tmp = 0
    j in (0,0)
    j in (1, 4)
    tmp + 1 + 1 = 2
    res [2]
loop 2:
    i = 1
    tmp = 0
    j in(0,1)
    j in (2，4) tmp + 1
    res [2, 1]
loop 3
    i = 2
    tmp = 0
    j in (0:2) tmp 0
    j in (3,4) tmp 0
    res [2,1,0]
loop 4
    i = 3
    tmp = 0
    j in (0，3) tmp + 3
    j in (4, 4) tmp + 0
    res [2,1,0,3]
'''
'''
B. optimized code
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums):  # return list[int]
        res = []
        for i in range(len(nums)):
            tmp = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    tmp += 1
            res.append(tmp)
        return res