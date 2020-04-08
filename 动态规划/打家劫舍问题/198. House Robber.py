#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 9:10
# @Author  : LI Dongdong
# @FileName: 198. House Robber.py
''''''
'''
题目概述：在一列数中取值，问值的最大值是多少，限制是不能有相邻的两个数
题目考点：dp
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: nums, list; length range from 0 to 1000; value range from 1 to 1000; order? N
output: the max amount; 
corner case:
    nums is None, return 0
    nums is  only one elem, return nums[0]

A. DP memo - dp(i) is that stole 1 to i house's max amout
    Method:
        1. corner case
        2. dp(i) = max(nums[i] + dp(i - 2))
        3. base case: dp(0) = 0
    Time complexity: O(n), n is house number
    Space: O(n)
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo = {}

        def dp(i):  # return max amount when can to i house
            if i in memo:
                return memo[i]
            if i <= 0:
                return 0

            res = max(dp(i - 1), nums[i - 1] + dp(i - 2))
            memo[i] = res
            return res

        return dp(n)


'''
DP table
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i - 2 >= 0:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            else:
                dp[i] = nums[i - 1]

        return dp[n]


'''
DP table
优化了空间，因为只用到了dp[i-1]和dp[i -2]
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp_i_1 = 0
        dp_i_2 = 0
        dp_i = 0

        for i in range(1, n + 1):
            dp_i = max(dp_i_1, dp_i_2 + nums[i - 1])
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i

        return dp_i