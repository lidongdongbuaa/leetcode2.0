#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 10:45
# @Author  : LI Dongdong
# @FileName: 55. Jump Game.py
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
input: list, length range is from 0 to inf; value range is from 0 to inf; have repeated, no order
output: True if can reach to end, else False
corner case:
    nums is None, return True


超时
i 是0-index坐标系下的位置
A. backtrack - find all possible combinations
    Method


'''


class Solution:
    def canJump(self, nums) -> bool:
        if not nums:
            return True

        n = len(nums)

        def backtrack(i):
            if i == n - 1:
                return True

            furtherJump = min(i + nums[i], n - 1)
            for j in range(i + 1, furtherJump + 1):
                if backtrack(j):
                    return True
            return False

        return backtrack(0)

'''
memo优化超时
'''


class Solution:
    def canJump(self, nums) -> bool:
        if not nums:
            return True

        n = len(nums)
        memo = {}

        def backtrack(i):
            if i in memo:
                return memo[i]
            if i == n - 1:
                return True

            res = False
            furtherJump = min(i + nums[i], n - 1)
            for j in range(i + 1, furtherJump + 1):
                if backtrack(j):
                    res = True
            memo[i] = res
            return memo[i]

        return backtrack(0)