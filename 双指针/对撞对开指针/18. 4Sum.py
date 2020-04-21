#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 14:58
# @Author  : LI Dongdong
# @FileName: 18. 4Sum.py
''''''
'''
题目概述：在重复元素的list里， 找四个数，让这四个数的和等于target
题目考点：基于two sum的对撞指针法
解决方案：2 for loop + 对撞对开指针
方法及方法分析：
time complexity order: O(n^3)
space complexity order: O(1)
如何考
'''
'''


input:
    nums; length range is from 4 to inf; have repeated value; no order
    target; int
output:
    list[list], if no result, return []
corner case
    nums lenght is 4
        if sum of them == target, return [nums]
        else, return []

A. brute force - use 4 for loop to scan every value
    Time complexity: O(n^4), n is length of nums
    Space: O(1)

B. two for loop + two pointer
    Time complexity: O(n^3)
    Space: O(n)

'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []

        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k, g = j + 1, n - 1
                while k < g:
                    total = nums[i] + nums[j] + nums[k] + nums[g]
                    if total < target:
                        k += 1
                    elif total == target:
                        res.add((nums[i], nums[j], nums[k], nums[g]))
                        k += 1
                        g -= 1
                    else:
                        g -= 1

        res = [list(elem) for elem in res]
        return res