#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 11:12
# @Author  : LI Dongdong
# @FileName: 16. 3Sum Closest.py
''''''
'''
题目概述：一列数中，求三数之和，其与target最相近
题目考点：two pointer法 对撞指针
解决方案：two pointer法
方法及方法分析：brute force + binary search; two pointer
time complexity order: two pointer O(n^2)
space complexity order: two pointer O(1)
如何考
'''
'''
input: nums, list; length range is from 3 to inf; have repeated value; no order
output: int
corner case:
    if length of nums is 3, return sum of nums

A. brute force + binary search
    method:
        1. list all possible combination sum of the three element in nums, save in list; tO(n^3)
        2. sort the list; tO(n^3log(n^3))
        3. use binary search to find the closest one tO(log(n^3))
    Time complexity: tO(n^3log(n^3)), n is length of nums
    Space: O(n^3)

B. two pointer search
    Method:
        1. sort the elem
        1. scan elem nums[i] in nums, set res = inf
            calculate the reduced value (target - nums[i]) as X
            use two pointer from left and right to center
                if left + right == X
                    return target
                elif left + right < x
                    renew res = min(abs(), res)
                    move left + 1
                else, renew res, move right - 1
        2. return res
    Time complexity: O(n^2)
    Space: O(1)

易错点：别忘记sort
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:  # corner case
            return sum(nums)

        nums.sort()

        res = float('inf')
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            X = target - nums[i]
            while j < k:
                if nums[j] + nums[k] < X:
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    j += 1
                elif nums[j] + nums[k] == X:
                    return target
                else:
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    k -= 1
        return res


'''
优化代码
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:  # corner case
            return sum(nums)

        nums.sort()

        res = float('inf')
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    j += 1
                elif total == target:
                    return target
                else:
                    k -= 1
        return res
