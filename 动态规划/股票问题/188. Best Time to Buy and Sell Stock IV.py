#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 11:54
# @Author  : LI Dongdong
# @FileName: 188. Best Time to Buy and Sell Stock IV.py
''''''
'''
题目概述：买卖最多k次
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
A. k is a large number
易错点：
    k很大，故k > n //2时，就相当于没有约束，此时递归不用k了，会节省内存；此时不能设置k = n//2, 因为这样运算次数还是太多
'''


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)
        memo = {}

        def dp(i, k, s):  # return most profit
            if (i, k, s) in memo:
                return memo[(i, k, s)]
            if i == 0 and s == 0:
                return 0
            if i == 0 and s == 1:
                return -prices[i]
            if k == 0 and s == 0:
                return 0
            if k == 0 and s == 1:
                return float('-inf')

            if s == 0:  # in ith day, not keep stack
                res = max(dp(i - 1, k, 0), prices[i] + dp(i - 1, k, 1))
            else:
                res = max(dp(i - 1, k - 1, 0) - prices[i], dp(i - 1, k, 1))
            memo[(i, k, s)] = res
            return res

        def dpInf(i, s):  # return most profit when k is larger than half of prices number
            if (i, s) in memo:
                return memo[(i, s)]
            if i == 0 and s == 0:
                return 0
            if i == 0 and s == 1:
                return -prices[0]

            if s == 0:
                res = max(dpInf(i - 1, 0), dpInf(i - 1, 1) + prices[i])
            else:
                res = max(dpInf(i - 1, 1), dpInf(i - 1, 0) - prices[i])
            memo[(i, s)] = res
            return res

        if k > n // 2:
            res = dpInf(n - 1, 0)
        else:
            res = dp(n - 1, k, 0)

        return res