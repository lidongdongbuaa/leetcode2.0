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
'''
input: 
    n, int; value range is from 0 to inf; 
    k, int; value range is from 0 to n
output; list[list], all combinations
corner case:
    if n == 0, return []
    if k == 1, return [[1],..., [n]]

Method: Backtrack
    1. use recursion to implement the backtrack
    2. use a path to record the scan elem, if len(path) == 2, append path to res
    3. return res

    Time complexity: O(n^2)
    Space: O(1) without output
    
易错点：思考tree结构的时候,backtrack里面参数的规则要一致，都从i开始取，或者i+ 1开始取
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0:  # corner case
            return []
        if k == 1:
            return [[elem] for elem in range(1, n + 1)]

        def backtrack(path, i):
            if len(path) == k:
                res.append(path[:])

            for j in range(i + 1, n + 1):
                path.append(j)
                backtrack(path, j)
                path.pop()

        res = []
        backtrack([], 0)
        return res