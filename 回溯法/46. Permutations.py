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

'''
input: list; lenght range of nums is from 0 to inf; not repeat; no order
output: list[list]
corner case
    nums is None, return []
    nums is only one element, return [[nums[0]]]

A. bracktracking
    Method:
        1. corner case
        2. use recursion and backtracking to push and pop the candidates
    Time complexity: O(2^n), n is length of nums
    Space: O(2^n)
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:  # corner case
            return []
        if len(nums) == 1:
            return [[nums[0]]]

        res = []

        n = len(nums)

        def backtrack(i, path):  # save all candidates in res list
            if i == n:
                res.append(path[:])
                return

            for x in nums:
                if x in path:
                    continue
                path.append(x)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res