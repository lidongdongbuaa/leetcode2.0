#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 11:12
# @Author  : LI Dongdong
# @FileName: 16. 3Sum Closest.py
''''''
'''
题目概述：一列数中，求三数之和，其与target最相近
题目考点：two pointer法 对撞对开指针
解决方案：two pointer法
方法及方法分析：brute force + binary search; two pointer
time complexity order: two pointer O(n^2)
space complexity order: two pointer O(1)
如何考
'''
'''
input: nums, list; length range is from 3 to inf; value range is -inf to inf; have repeated value; no order
output: int
corner case: if len(nums) == 3, return sum(nums)

sort + two pointer
Steps:
    1. sort the nums
    2. traverse i from 0 to n - 3
        left = target - nums[i]
        two pointer to find j and k in [i + 1, n]
            calculate sum of k and j sum, and renew the res
    3. return res
    
    Time complexity: O(n^2)
    Spac: O(n)
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)

        nums.sort()
        i = 0
        res = float('inf')
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    j += 1
                elif total == target:
                    return total
                else:
                    k -= 1
            i += 1
        return res
