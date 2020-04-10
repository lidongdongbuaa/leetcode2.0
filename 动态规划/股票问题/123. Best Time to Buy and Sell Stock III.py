#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 8:55
# @Author  : LI Dongdong
# @FileName: 123. Best Time to Buy and Sell Stock III.py
''''''
'''
题目概述：只能买卖两次
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
dp(i, k, s)
买入的时候：k+1，总盈利减去买入价
卖出的时候：k不变，总盈利加入卖出价
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        memo = {}

        def dp(i, k, s):  # return max amount
            if (i, k, s) in memo:
                return memo[(i, k, s)]
            if i == 0 and s == 0:
                return 0
            if i == 0 and s == 1:
                return -prices[0]
            if k == 0 and s == 0:
                return 0
            if k == 0 and s == 1:
                return float('-inf')

            if s == 0:
                res = max(dp(i - 1, k, 0), dp(i - 1, k, 1) + prices[i])
            else:
                res = max(dp(i - 1, k, 1), dp(i - 1, k - 1, 0) - prices[i])
            memo[(i, k, s)] = res
            return res

        return dp(len(prices) - 1, 2, 0)


'''
DP table 
    在dp for循环里，进行初始值的赋予
    dp[i][k][s]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]  # i, k, s

        for i in range(n):
            for k in range(3):
                for s in range(2):
                    if i == 0 and s == 0:
                        dp[i][k][s] = 0
                    elif i == 0 and s == 1:
                        dp[i][k][s] = -prices[0]
                    elif k == 0 and s == 0:
                        dp[i][k][s] = 0
                    elif k == 0 and s == 1:
                        dp[i][k][s] = float('-inf')
                    else:
                        if s == 0:
                            dp[i][k][s] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                        else:
                            dp[i][k][s] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][2][0]


'''
DP table 
    在dp for循环里，进行初始值的赋予
    dp[i][k][s]
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]  # i, k, s

        for i in range(n):
            for k in range(3):
                dp[0][k][0] = 0
                dp[0][k][1] = -prices[0]
                dp[i][0][0] = 0
                dp[i][0][1] = float('-inf')

                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][2][0]
