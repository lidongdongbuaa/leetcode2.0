#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 20:10
# @Author  : LI Dongdong
# @FileName: 322. Coin Change.py
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
input: 
    coins, list; length range is from 0 to 1000; value is more than 0? Y; repeated? N; order? Y
    amount, int; more than 0? Y
output:   
    fewest number of coin, int; no money, return -1
corner case:
    coins is None, return -1
    amount is 0 or None, return -1
    coins is only one, amount is only one, same, return 1; else return -1

A. DP - dp(i) is min coins number to make up i 
    Method:
        1. corner case
        2. dp[i] = min(dp[i - coin[0]], dp[i - coin[1]],...dp[i - coin[n-1]]) +  1
        3. base case,  dp[0] = 0, dp[coin[i]] = 1
    
time complexity: O(sn) s is amount, n is denomination count, 一共有s个子问题，每个子问题n个for循环
Space:O(s)
易错点：
    1. 求最小值，初始化为正无穷
    2. dp[coins[i]] = 1可以不用设定，因为设定dp[0] = 0了，可以通过此进行计算
    3. dp循环里的求最小值res = min(nums[i], nums[i +1], nums[i + 2],....)一般通过for i in X, res = min(res, i)进行实现
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:  # corner case
            return -1
        if not amount:
            return 0

        if len(coins) == 1 and amount % coins[0] == 0:
            return amount // coins[0]
        elif len(coins) == 1 and amount % coins[0] != 0:
            return -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # for x in coins:
        #     if x <= amount:
        #         dp[x] = 1

        for i in range(amount + 1):
            for x in coins:
                # if x <= amount:
                if i - x >= 0:
                    dp[i] = min(dp[i], dp[i - x] + 1)

        if dp[amount] ==  float('inf'):
            return -1
        else:
            return dp[amount]


'''
备忘录写法
time complexity: O(sn) s is amount, n is denomination count
Space:O(s)
易错点：
    1. 考虑到i等于0和小于0的情况
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:  # corner case
            return -1
        if not amount:
            return 0

        memo = {}

        def dp(i):  # return min coins number of i
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            if i < 0:
                return float('inf')

            res = float('inf')
            for x in coins:
                res = min(dp(i - x) + 1, res)
            memo[i] = res
            return res

        res = dp(amount)
        if res == float('inf'):
            return -1
        else:
            return res