#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 21:31
# @Author  : LI Dongdong
# @FileName: 78. Subsets.py
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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, start, nums):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1, nums)
                path.pop()

        backtrack([], 0, nums)
        return res
