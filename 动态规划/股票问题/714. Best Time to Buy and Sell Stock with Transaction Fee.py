#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 11:55
# @Author  : LI Dongdong
# @FileName: 714. Best Time to Buy and Sell Stock with Transaction Fee.py
''''''
'''
题目概述：不限次数，买卖有手续费
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
                res = max(dp(i - 1, 0), dp(i - 1, 1) + prices[i] - fee)
            else:
                res = max(dp(i - 1, 1), dp(i - 1, 0) - prices[i])
            memo[(i, s)] = res
            return res

        return dp(n - 1, 0)

'''
DP table
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_1 + prices[i] - fee, dp_i_0)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0