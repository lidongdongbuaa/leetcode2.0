#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 11:46
# @Author  : LI Dongdong
# @FileName: 01背包问题.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
算法返回 6，选择前两件物品装进背包，总重量 3 小于 W，可以获得最大价值 6。
'''

'''
明确两点，状态和选择
1. 能装的价值由载重量W和选哪N个物品共同决定（因为物品不能重复，选完一个之后，不能再选另一个，故对价值产生影响）
    故状态是 背包的容量和可选择的物品
2. 选择就是 物品list里的i物品装不装进背包

dp数组的定义 - 
1. dp[i][w] = 对于前i个物品，在w载重的要求下，达到的最大价值
2. base case, dp[0][w] = 0, dp[i][0] = 0

状态转移方程
1.不放物品i情况下：
    dp[i][w] = dp[i - 1][w]
2.放物品i的情况下：
    dp[i][w] = max(dp[i - 1][w - wt(i)] + wt(i))
    
易错点： 先判断是否有小于0的，再判断是否等于0；因为等于0时，可包含小于0的状态
'''

class DP:
    def backpack01(self, n, W, wt, val):  # return max value in weight range
        def dp(i, w):
            if i < 0 or w < 0:
                return float('-inf')
            if i == 0 or w == 0:
                return 0

            res = float('-inf')
            res = max(res, dp(i - 1, w), dp(i - 1, w - wt[i - 1]) + val[i - 1])
            return res

        return dp(n, W)
x = DP()
print(x.backpack01(n = 3, W = 4, wt = [2, 1, 3], val = [4, 2, 3]))

'''
用memo优化
'''
class DP:
    def backpack01(self, n, W, wt, val):  # return max value in weight range
        if not wt or not val:
            return 0
        if n == 0 or W == 0:
            return 0

        memo = {}
        def dp(i, w):
            if (i, w) in memo:
                return memo[(i, w)]

            if i < 0 or w < 0:
                return float('-inf')
            if i == 0 or w == 0:
                return 0

            res = float('-inf')
            res = max(res, dp(i - 1, w), dp(i - 1, w - wt[i - 1]) + val[i - 1])
            memo[(i, w)] = res
            return res

        return dp(n, W)

x = DP()
print(x.backpack01(n = 3, W = 4, wt = [2, 1, 3], val = [4, 2, 3]))

'''
dp table 优化
易错点： 对w - wt[i - 1] < 0进行判断，此时不能选i
'''
class DP:
    def backpack01(self, n, W, wt, val):  # return max value in weight range
        if not wt or not val:
            return 0
        if n == 0 or W == 0:
            return 0

        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if w - wt[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
        return dp[n][W]

x = DP()
print(x.backpack01(n=3, W=4, wt=[2, 1, 3], val=[4, 2, 3]))