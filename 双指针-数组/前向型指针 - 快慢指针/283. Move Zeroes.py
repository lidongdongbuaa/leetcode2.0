#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 10:00
# @Author  : LI Dongdong
# @FileName: 283. Move Zeroes.py
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
input: nums; length range is from 0 to inf; value range is no limit; have repeated; no order
output: None
corner case: 
    nums is None, return None

A. slow - fast pointer - f search for no-Zero value
    Method:
        1. set s = 0, f as 0； s 保持为待修改的状态位置
        2. while f < n
            if nums[f] == 0
                f += 1
            else
                nums[s] = nums[f]
                s += 1，# s 依旧保持原位性
                f += 1
    Time complexity: O(n)
    Space: O(1)

 [1,3,12,3,12]
      s
              f
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        s, f = 0, 0
        n = len(nums)

        while f < n:
            if nums[f] == 0:
                f += 1
            else:
                nums[s] = nums[f]
                s += 1  # s是待修改的状态
                f += 1

        while s < n:
            nums[s] = 0
            s += 1
