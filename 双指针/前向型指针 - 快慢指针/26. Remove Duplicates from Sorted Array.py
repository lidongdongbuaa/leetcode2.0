#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 11:54
# @Author  : LI Dongdong
# @FileName: 26. Remove Duplicates from Sorted Array.py
''''''
'''
题目概述：原位删除重复的数组，输出不重复value的数量
题目考点：前向型指针 - 快慢指针
解决方案：前向型指针 - 快慢指针，遇到不同的值的时候，s进一位，并修改为该不同的值
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: nums, list; length range is from 0 to inf; no value range; have repeated value; increasing order
output: int, length of no duplicated length
corner case
    if nums is no, return 0
    if nums is only one elem, return 1

A. two pointer - slow and fast pointer
    Method:
        1. set slow and fast pointer at 0 index and 1 index position
            slow(s) is 0, value = 0; fast(f) = 1,value = 0
        2. while f reach to end of nums
            a. if s value = f value, move f to next position
                move f to next index, 2
                s step forward, modify s as f value 
                s is 1, nums[s] = 2  ->[1,2,2]
            b. cotinue a step
        3.return s + 1
    Time complexity:O(N), N is length of nums
    Space: O(1)
易错点： 
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0
        if len(nums) == 1:
            return 1

        s, f = 0, 1
        n = len(nums)
        while f <= n - 1:
            while nums[s] == nums[f]:
                f += 1
                if f == n:
                    return s + 1
            s += 1
            nums[s] = nums[f]
        return s + 1


'''
  [0,1,2,3,4,2,2,3,3,4]
           s 
                      f
  [1,2,2]
     s
        f
'''
'''
优化的代码
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0
        if len(nums) == 1:
            return 1

        s, f = 0, 0
        n = len(nums)

        while f < n:
            if nums[s] == nums[f]:
                f += 1
            else:
                s += 1
                nums[s] = nums[f]
                f += 1
        return s + 1
