#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 20:23
# @Author  : LI Dongdong
# @FileName: 46. Permutations.py
''''''
'''
题目概述：求数组的全排列
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, nums):

            for i in nums:
                if i in path:
                    continue
                path.append(i)
                if len(path) == len(nums):
                    res.append(path[:])
                backtrack(path, nums)
                path.pop()

        backtrack([], nums)
        return res