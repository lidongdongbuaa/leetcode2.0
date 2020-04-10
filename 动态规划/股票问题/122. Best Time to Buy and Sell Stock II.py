#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 20:56
# @Author  : LI Dongdong
# @FileName: 122. Best Time to Buy and Sell Stock II.py
''''''
'''
题目概述：不限次数
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: prices, list; length range is from 1 to 3*10^4; elements value range is from 0 to 10^4; repeated? Yes; order? N
output: max amount, int
corner case:
    prices is only one elements, return 0

A. brute force - accumulate the end - start gap of increasing part of prices
    Method:
        1. corner case
        2. set first and second pointer to find the first and end value of the increasing part
            e.g 1-5, 3-6
        3. calculate the gap between them

    Time complexity: O(N)
    Space: O(1)

B. DP - dp[i][k][s] is on i-th day, k times transations, stack is s situaiton(have or not), the max amount value
    Method:
        1. corner case
        2. 
            if s = 0, no stack
                dp(i,k, s) = max(dp(i - 1, k, 1) + prices[i], dp(i- 1, k, 0))
            if s = 1, have stack
                dp(i, k, s) = max(dp(i - 1, k -1, 0) - prices[i], dp(i -1, k, 1))
        3. base case
            i = 0, s = 0, return 0
            i = 0, s = 1, return -price[0]
            k = 0, s = 0, return 0
            k = 0, s = 1, return float('-inf')
    Time complexity: O(n * n/2 * 2) = (n^2)
    Space: O(2*n^2) = O(n^2)

C. DP - dp[i][s] is on i-th day, stack is s situaiton(have or not), the max amount value
    Method:
        1. corner case
        2. state transmission equation
            if s = 0
                dp(i, s) = max(dp(i - 1, 1) + prices[i], dp(i - 1, s))
            if s = 1
                dp(i, s) = max(dp(i - 1, 1), dp(i - 1, 0) - price[i])
        3. base case
            i = 0, s = 0, return 0
            i = 0, s = 1, return -prices[0]
易错点：与k=1的区别是，本题中s = 1时，当新加i时，有前序的dp(i - 1, 0)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        memo = {}

        def dp(i, s):  # return max amount
            if (i, s) in memo:
                return memo[(i, s)]

            if i == 0 and s == 0:
                return 0
            if i == 0 and s == 1:
                return -prices[0]

            if s == 0:  # no stack
                res = max(dp(i - 1, 0), dp(i - 1, 1) + prices[i])
            else:  # have stack
                res = max(dp(i - 1, 1), dp(i - 1, 0) - prices[i])
            memo[(i, s)] = res
            return res

        return dp(len(prices) - 1, 0)


'''
D. DP - dp[i][s] is on i-th day, stack is s situaiton(have or not), the max amount value
    Method:
        1. corner case
        2. state transmission equation
            if s = 0
                dp(i, 0) = max(dp(i - 1, 1) + prices[i], dp(i - 1, 0))
            if s = 1
                dp(i, 1) = max(dp(i - 1, 1), dp(i - 1, 0) - price[i])
        3. base case
            i = 0, s = 0, return 0
            i = 0, s = 1, return -prices[0]
易错点：dp_i_0, i代表不同的价格，0/1代表是否有stack
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_1 + prices[i], dp_i_0)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0


'''
D. DP - dp[i][s] is on i-th day, stack is s situaiton(have or not), the max amount value
    Method:
        1. corner case
        2. state transmission equation
            if s = 0
                dp(i, 0) = max(dp(i - 1, 1) + prices[i], dp(i - 1, 0))
            if s = 1
                dp(i, 1) = max(dp(i - 1, 1), dp(i - 1, 0) - price[i])
        3. base case
            i = 0, s = 0, return 0
            i = 0, s = 1, return -prices[0]
易错点：
    1. dp_i_0, i代表不同的价格，0/1代表是否有stack
    2. 建立tmp，在计算新的dp_i_0之前，保存dp_i_0, 供dp_i_1使用
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, len(prices)):
            dp_i_0, dp_i_1 = max(dp_i_1 + prices[i], dp_i_0), max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0