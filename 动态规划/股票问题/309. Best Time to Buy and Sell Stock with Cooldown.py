#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 11:55
# @Author  : LI Dongdong
# @FileName: 309. Best Time to Buy and Sell Stock with Cooldown.py
''''''
'''
题目概述：不限次数，买卖有冷冻期
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
A. DP
    if s == 0
        dp[i][s] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    else:
        dp[i][s] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        n = len(prices)

        memo = {}

        def dp(i, s):  # return max amount
            if (i, s) in memo:
                return memo[(i, s)]

            if i <= 0 and s == 0:
                return 0
            if i <= 0 and s == 1:
                return -prices[0]

            if s == 0:
                res = max(dp(i - 1, 0), dp(i - 1, 1) + prices[i])
            else:
                res = max(dp(i - 1, 1), dp(i - 2, 0) - prices[i])
            memo[(i, s)] = res
            return res

        return dp(n - 1, 0)

