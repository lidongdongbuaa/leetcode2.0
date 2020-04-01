#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 21:31
# @Author  : LI Dongdong
# @FileName: 78. Subsets.py
''''''
'''
题目概述：求一个序列的所有子集
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
A. math idea 
数学归纳法
Time:O(2^n * n), product 2^n subset, add to res O(N)
Space:O(2^n * n)
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        n = len(nums)
        res = [[]]

        for elem in nums:
            res += [i + [elem] for i in res]

        return res


'''
backtracking
Time:O(N * 2^N)，backtrack运行了2^N次，path[:]的复杂度为N
Space: O(N * 2^N)，2^N个subset，每个subset占据N空间
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
