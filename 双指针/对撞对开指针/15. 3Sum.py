#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 10:09
# @Author  : LI Dongdong
# @FileName: 15. 3Sum.py
''''''
'''
题目概述：在一列含有重复元素的list里，找到和等于0的不重复的子集
题目考点：two pointer; set去重
优化核心：判断nums[i]是否重复，若重复，及时跳过；判断nums[i]是否 < 0
易错点：返回值是list
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
'''


'''
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
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <= 2:
            return []

        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0: # 优化的关键
                break
            if i >= 1 and nums[i] == nums[i - 1]:  # 优化的关键
                continue
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                else:
                    k -= 1
        return [list(elem) for elem in res]

'''
sort + two sum dic 法
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <= 2:
            return []

        nums.sort()
        res = set()
        for i, val in enumerate(nums[:-2]):
            if val > 0: # 优化的关键
                break
            if i >= 1 and val == nums[i - 1]:  # 优化的关键
                continue
            t = - val
            d = set()
            for elem in nums[i + 1:]:
                if (t - elem) in d:
                    res.add((val, elem, t - elem))
                else:
                    d.add(elem)
        return [list(elem) for elem in res]