#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 10:09
# @Author  : LI Dongdong
# @FileName: 15. 3Sum.py
''''''
'''
题目概述：在一列含有重复元素的list里，找到和等于0的不重复的子集
题目考点：two pointer; set去重；
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
三数之和：固定一个，找另外两个

input:
    nums: list; length range is from 3 to inf; value range is inf; have repeated value; no order
output:
    list[list], no repeated
corner case
    if len(nums)== 3 and sum(nums) == 0, return [nums]
    if sum(nums) != 0, return []

sort + two pointer
Steps:
    1. sort the nums
    2. traversal i in nums range, until nums[i] > 0
        two pointer method to find j and k in nums[i + 1:]
        if sum of j and k == -nums[i] and [nums[i], nums[j], nums[k]] not in res, append it to res
    3. return res
    Time complexity: O(nlogn + n^2) = O(n^2)
    Space: O(n)
易错点：
    1. nums[i] <= 0
    2. i += 1
    3，注意返回值的格式
    
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        if len(nums) == 3 and sum(nums) != 0:
            return []

        n = len(nums)
        nums.sort()
        i = 0
        res = set()
        while i < n and nums[i] <= 0:
            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                else:
                    k -= 1
            i += 1

        return [list(item) for item in res]
'''
Given array nums = [-1, 0, 1, 2, -1, -4]

n = len(nums) = 6 > 3

nums.sort = [-4, -1, -1, 0, 1, 2]
[-4, -1, -1, 0, 1, 2] 
             i
             j
                   k
target = 1
total = 1
res = [[-1, -1, 2], [-1, 0, 1]]
'''