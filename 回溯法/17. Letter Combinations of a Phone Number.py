#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 23:16
# @Author  : LI Dongdong
# @FileName: 17. Letter Combinations of a Phone Number.py
''''''
'''
题目概述：多个arr， 每个取一个，求不同的组合
题目考点：回溯
解决方案：回溯模板1
方法及方法分析：回溯法
time complexity order: 
space complexity order: 
如何考
'''
'''
A. backtrack
    Method:
        1. transfer number to string list
            23 - [[a,b, c],[d,e,f]]
        2. assume the problem as tree, [] is first level, a ,b,c is second level...to do backtrack
    Time complexity: O(3^n), n is length of digits
    Space: O(3^n)
'''


class Solution:
    def letterCombinations(self, digits: str):
        tag = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        strList = [tag[elem] for elem in digits]

        m = len(digits)

        def backtrack(start, path):  # save all combinations in res
            if start > m - 1:
                return

            for i in range(len(strList[start])):
                path.append(strList[start][i])
                if len(path) == m:
                    res.append(path[:])
                backtrack(start + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        res = [''.join(elem) for elem in res]
        return res

