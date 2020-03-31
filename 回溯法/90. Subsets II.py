#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 21:31
# @Author  : LI Dongdong
# @FileName: 90. Subsets II.py
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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, path, nums):  # save all path in res
            if path not in res:
                res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path, nums)
                path.pop()

        backtrack(0, [], nums)
        return res

