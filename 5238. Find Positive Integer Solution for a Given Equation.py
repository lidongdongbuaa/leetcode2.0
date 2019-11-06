#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 11:58
# @Author  : LI Dongdong
# @FileName: 5238. Find Positive Integer Solution for a Given Equation.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
法
思路：
方法：
边界条件：
time complex: 
space complex: 
'''

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        i = 1
        j = 1000
        stack = []
        while i < j:
            result = customfunction.f(i, j)
            if result == z:
                stack.append([i, j])
            elif result < z:
                i = i + 1
            elif result > z:
                j = j - 1
        return stack