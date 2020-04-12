#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 9:04
# @Author  : LI Dongdong
# @FileName: 121. Best Time to Buy and Sell Stock.py
''''''
'''
题目概述：买卖限制为一次；取一列数里的两个数a,b，求这两个数的正方向差 b-a最大是多少
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: list; the length range from 0 to 1000; element value range from 1 to max; repeated, yes; order, NO
output: int, increasing max gap; if no increasing, return 0
corner case:
    input is None, return 0
    input is only one, return 0

A. brute force - compare increasing i and j, find the max result
    Time complexity: (n ^ 2)
    Space: O(1)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        res = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                pre = prices[i]
                cur = prices[j]
                if pre < cur and res < (cur - pre):
                    res = cur - pre
        return res


'''
B. 3D DP - DP[i][k][s] is in ith day, transmission k times, keep stack situation s, the most profit
    Method:
        1. corner case
        2. if keep stack
                dp[i][k][1] = max(dp[i- 1][k - 1][0] - price, dp[i - 1][k][1])
            else:
                dp[i][k][0] = max(dp[i- 1][k][1] + price, dp[i - 1][k][0])
        3. base case
易错点：
    针对实际的情况，各个参数为0的状况，考虑完整的边界条件
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)
        K = 1
        S = 0
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

        return dp(n - 1, K, S)
'''
C. 2D dp memo - dp(i, s) is on ith day, s situation, the most amount
    method:
        1. corner case
        2. dp 
            if s == 0:
                dp(i,0) = max(dp(i - 1, 1) + prices[i], dp(i - 1, 0))
            else:
                dp(i, 1) = max(dp(i - 1, 1), dp(i - 1, 0) - prices[i])
        3. base case
                i < 0, dp = 0
    Time complexity: O(2*n), n is number of days
    Space: O(n)

易错点：
    1. if i = 0， s = 1时，返回扣除第一个值的价格
    2. 明确dp(i - 1, 0)为0，故不参与dp(i, 1)的状态转移方程
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        memo = {}

        def dp(i, s):  # return ith day most amount under s situation which is 0/1 - keep or not keep the stack
            if (i, s) in memo:
                return memo[(i, s)]

            if i == 0 and s == 0:
                return 0
            if i == 0 and s == 1:
                return -prices[0]

            if s == 0:
                res = max(dp(i - 1, 1) + prices[i], dp(i - 1, 0))
            else:
                res = max(dp(i - 1, 1), - prices[i])
            memo[(i, s)] = res
            return res

        return dp(len(prices) - 1, 0)


'''
D. 2D dp table - dp(i, s) is on ith day, s situation, the most amount
    method:
        1. corner case
        2. dp 
            if s == 0:
                dp(i,0) = max(dp(i - 1, 1) + prices[i], dp(i - 1, 0))
            else:
                dp(i, 1) = max(dp(i - 1, 1), - prices[i])
        3. base case
             if i == 0 and s == 0:  0
            if i == 0 and s == 1: -prices[0]
    Time complexity: O(2*n), n is number of days
    Space: O(n)
易错点：在dp(i,1)时，应该是-prices[i], 而不是dp[i - 1, 0] =》 代码要及时删除冗余的部分
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], - prices[i])

        return dp[n - 1][0]


'''
E. 2D dp table, 增加0列版 - dp(i, s) is on ith day, s situation, the most amount
易错点：
    1. 增加不存在空列时
        * 边界条件是不存在情况下的dp值
        * for中，变量从起始值开始循环
    2. 不增加空列时
        * 边界条件时变量等于起始值下的dp值
        * for中，变量从第二个值开始循环

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 0
        dp[0][1] = float('-inf')

        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], - prices[i - 1])

        return dp[n][0]


'''
E. 2D dp table,优化空间 - dp(i, s) is on ith day, s situation, the most amount
Time：O(2*n)
Space: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:  # corner case
            return 0

        n = len(prices)

        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, n):
            dp_i_0 = max(dp_i_1 + prices[i], dp_i_0)
            dp_i_1 = max(dp_i_1, - prices[i])

        return dp_i_0

