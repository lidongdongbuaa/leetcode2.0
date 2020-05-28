#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 11:12
# @Author  : LI Dongdong
# @FileName: 16. 3Sum Closest.py
''''''
'''
题目概述：一列数中，求三数之和，其与target最相近
题目考点：two pointer法 对撞对开指针
优化核心：排除重复的i；sum = target时，及时返回
易错点：
方法及方法分析：
time complexity order: O(n^2)
space complexity order: O(1)
如何考
'''
'''
input: nums, list, length range is from 3 to 10^3, value range is inf; have repeated value; no order
    target: range value is inf
output: int
corner case
    nums length is 3, return sum of nums

two pointers
Step:
1. sort the nums, res = 0, gap = inf
2. traverse i th elem in nums[:-2]
    if i >= 1 and i elem = i - 1 elem, continue
    two pointer, j, k from i + 1, n - 1 th elem, move towards each other
        if i, j, k elem sum > target, move k to left, if new gap < gap, renew res
        if equal, return target
        if sum < target, move i to right, if new gap < gap, renew res
3. return res

Time complexity: O(nlogn + n^2)
Space: O(n) store the sorted nums


'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:  # corner case
            return sum(nums)

        nums.sort()
        res = 0
        gap = float('inf')

        for i, v in enumerate(nums[:-2]):
            if i > 1 and nums[i] == nums[i - 1]:  # 排除重复的值
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > target:
                    k -= 1
                elif total == target:
                    return target
                else:
                    j += 1
                if abs(total - target) < gap:
                    gap = abs(total - target)
                    res = total
        return res
