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
input: nums, list; length range is from 3 to inf; have repeat value; no order
output: list[list], represent the value of nums
corner case:
    nums length is 3, return [nums]

A.brute force - use 3 for loop to find three values
    Time complexity: O(n^3)
    Space: O(1)

B.two pointer - use one for loop, and use two pointer find other 2 value
    Method: 
        1. corner case
        2. sort nums
        3. scan elem x from index 0 to index (lenght - 3)
            scan other two value in right range of nums by two pointer
                if sum equal to 0, and x and two value not in result
                    add (x, two value) in res
        4. return res
    Time complexity: O(n^2)
    space: (1)
易错点：
    1. 用set + tuple去重
    2. 在leftSum == -nums[i]时，即使不加入res里面，j,k也要move
    3. 存在不存在的情况，返回[]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:  # corner case
            return [nums]

        nums.sort()

        res = set()
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                leftSum = nums[j] + nums[k]
                if leftSum < -nums[i]:
                    j += 1
                elif leftSum == -nums[i]:
                    if (nums[i], nums[j], nums[k]) not in res:
                        res.add((nums[i], nums[j], nums[k]))
                    j += 1  # 易错点
                    k -= 1
                else:
                    k -= 1
        return list(res)

'''
优化代码
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:  # corner case
            return [nums]

        nums.sort()

        res = set()
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total == 0:
                    if (nums[i], nums[j], nums[k]) not in res:
                        res.add((nums[i], nums[j], nums[k]))
                    j += 1  # 易错点
                    k -= 1
                else:
                    k -= 1
        return list(res)