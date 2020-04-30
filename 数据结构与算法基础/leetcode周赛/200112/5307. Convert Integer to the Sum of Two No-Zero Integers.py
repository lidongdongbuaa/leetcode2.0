#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 11:44
# @Author  : LI Dongdong
# @FileName: 5307. Convert Integer to the Sum of Two No-Zero Integers.py
''''''
'''
题目分析
1.要求：Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.
Return a list of two integers [A, B] where:
A and B are No-Zero integers. A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.
Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
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
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        mid = n//2
        for x in range(1, mid + 1):
            if '0' not in str(x) and '0' not in str(n - x):
                return [x, n - x]