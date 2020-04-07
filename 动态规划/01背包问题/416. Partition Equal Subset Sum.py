#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 21:44
# @Author  : LI Dongdong
# @FileName: 416. Partition Equal Subset Sum.py
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
求有没有数的和可以到达sum的一半

input:
    nums, list; positive; length range from 0 t 200; value range, from 0 to 100
output:
    True if we can divide them, else return False
corner case
    nums is None, return True
    nums is only one element, return False
    sum of nums is odd, return False

A. brute force - backtrack find the suitable subset
Time complexity: O(2^n)
Space: O(2^n)

从input里拿数字，放到背包中，看能否让背包的值为sum的一半
能否成功，由sum值的一半和选那几个input共同决定；选择就是是否选input里的值


B. DP - dp(i, w), for input[:i] and w value, the if input[:i] can make up w, return True
    Method:
        1. corner case
        2. dp(i, w) = dp(i-1, w) and dp(i - 1, w - input[i - 1])
        3. base case, if i <= 0 or w <= 0 return False

'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:  # corner case
            return True
        if len(nums) == 1:
            return False
        if sum(nums) % 2 != 0:
            return False

        numb = sum(nums) // 2

        memo = {}

        def dp(i, w):  # return True if sum == numb
            if (i, w) in memo:
                return memo[(i, w)]

            if i == 0 and w == 0:
                return True
            if i <= 0 or w <= 0:
                return False

            res = dp(i - 1, w) or dp(i - 1, w - nums[i - 1])
            memo[(i, w)] = res
            return res

        return dp(len(nums), numb)

