#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 11:54
# @Author  : LI Dongdong
# @FileName: 63. Unique Paths II.py
''''''
'''
题目概述：求左上角到右下角的所有路径，路径中有障碍1
题目考点：dp + 在dp中有障碍
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: matrix; including only 0 and 1; size range of matrix is 0*0 to m * n
output: integer, the number of path
corner case: 
    gird is None or [[]], return 0

A. backtrack - find path and return path numbers
    method:
        1. corner case
        2. use dfs to explore all path, backtrack to record the path
            if reach to the end, save path in res
        3. return length of the res
    Time complexity: O(2^(m * n))
    Space: O(m + n) recursion stack used



B. DP - dp(i, j) is the number of path when reach to i,j cell
    Method:
        1. corner case
        2. function: 
            if gird[i][j] == 0
                dp(i,j) = max(dp(i -1, j), dp(i, j - 1), dp(i - 1, j) + dp(i, j - 1))
            else:
                dp(i,j) = float('-inf')
        3. base case,
            i or j < 0
            i = j = 0, grid[i][j] = 1/0
    Time complexity: O(m * n)
    Space: O(m * n)

困难点：矩阵时的base case 
 '''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid == [[]]:
            return 0

        grid = obstacleGrid

        m, n = len(grid), len(grid[0])

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 or j < 0:
                return float('-inf')
            if i == 0 and j == 0 and grid[i][j] == 1:
                return float('-inf')
            if i == 0 and j == 0 and grid[i][j] == 0:
                return 1

            if grid[i][j] == 1:
                res = float('-inf')
            else:
                res = max(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j) + dp(i, j - 1))

            memo[(i, j)] = res
            return res

        res = dp(m - 1, n - 1)
        if res == float('-inf'):
            return 0
        else:
            return res
'''
DP Table
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid == [[]]:
            return 0

        grid = obstacleGrid

        m, n = len(grid), len(grid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1 and grid[i - 1][j - 1] == 0:
                    dp[i][j] = 1
                elif grid[i - 1][j - 1] == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j] + dp[i][j - 1])
                elif grid[i - 1][j - 1] == 1:
                    dp[i][j] = float('-inf')

        res = dp[m][n]
        if res == float('-inf'):
            return 0
        else:
            return res
