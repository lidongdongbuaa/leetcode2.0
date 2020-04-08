#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 10:59
# @Author  : LI Dongdong
# @FileName: 213. House Robber II.py
''''''
'''
题目概述：打家劫舍，但是家是环状的
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
house is in cycle, so cann't rob first house and end house at the same time

input: nums, list; lenght range from 0 to 1000; value range from 1 to 1000
output: max amount, int
corner case: 
    nums is None, return 0
    nums is only one element, return nums[0]

A. DP - dp[i] is that until i house, the max amount the robber can rob; considering input[0:n-1], input[1:n]
    Method

    Time complexlity:O(N)
    Space complexity: O(N)
易错点：不需要res = float('-inf')
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        memo = {}
        def dp(start, i):  # return max amount in range start and i
            if (start, i) in memo:
                return memo[(start, i)]
            if i <= start - 1:
                return 0

            res = max(dp(start, i - 1), dp(start,  i - 2) + nums[i - 1])
            memo[(start, i)] = res
            return res

        return max(dp(1, n - 1), dp(2, n))

'''
B DP table
    Method: dp[i] = max(dp[i - 1], nums[i - 1] + dp(i - 2))
易错点：i - 2 < 0，时 dp[i] != 0, 此时i只等于1，故等于arr[0], 或者max(dp[i - 1], arr[i - 1] + dp[i - 2])中，直接消除dp[i - 2]
    Time: O(n), n is length of nums
    Space: O(n)
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0
        if len(nums) == 1:
            return nums[0]

        def dp(arr):  # return arr's max amount
            n = len(arr)

            dp = [0] * (n + 1)

            for i in range(1, n + 1):
                if i - 2 < 0:
                    dp[i] = max(arr[i - 1], dp[i - 1])
                else:
                    dp[i] = max(dp[i - 1], arr[i - 1] + dp[i - 2])
            return dp[n]

        return max(dp(nums[:-1]), dp(nums[1:]))