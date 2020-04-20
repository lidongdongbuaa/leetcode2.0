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
'''
corner case
    nums is None, return []

A. backtrack
    Method:
        1. 先对nums排序
        1.  set res list to save the result
        2. use backtrack(index, path) to get the subset
            a. if path not in res, append path in res
            b. scan elem from index to end in nums
                append elem in path
                backtrack(index + 1, path)
                pop elem in path
        Time complexity: O(2^n * n), n is copy time, 2^n is number of subset
        Space: O(2^n * n), n is lenght of one subset

这一题的result里不能有重复的subset，即[4,1], [1, 4]视为重复，故两种方案
    1. set, 本题要pop，不适用
    2. sublist in list, 由于本题输入是乱序，故sublist可能出现[4,1,4], [1,4,4]的情况，故in list 不起作用
        故采用先sort nums,让sublist不可能出现前面的情况。
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:  # corner case
            return []

        res = []
        n = len(nums)
        nums.sort()

        def backtrack(i, path):  # save all no-duplicate subset in res
            if path not in res:
                res.append(path[:])

            for j in range(i, n):
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()

        backtrack(0, [])
        return res

