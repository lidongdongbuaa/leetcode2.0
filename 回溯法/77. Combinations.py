#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 22:02
# @Author  : LI Dongdong
# @FileName: 77. Combinations.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, n, k):
            if len(path) == k:
                res.append(path[:])

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path, n, k)
                path.pop()

        backtrack(1, [], n, k)
        return res