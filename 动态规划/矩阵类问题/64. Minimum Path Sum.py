#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 8:34
# @Author  : LI Dongdong
# @FileName: 64. Minimum Path Sum.py
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
input: matrix, size range is from 0*0 to 1000; have repeat value; no order
output: integer of the path sum
corner: 
    the grid is None or [[]], return 0
    the grid is only one elem, return grid[0][0]

A. DP - dp(i, j) is the min sum of path when reaching to i, j cell
    Method:
        1. corner case
        2. function:
            dp(i, j) = min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
        3. base case
            if i or j < 0, return float('inf')
            if i = 0 and j = 0, return grid[0][0]
        4 use memo as dict to save space and time

    Time complexity: O(m*n) m is row number, n is columns number
    Space complexity: O(m + n), recursion stack used, only left and down direction
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or grid == [[]]:  # corner case
            return 0

        memo = {}
        m, n = len(grid), len(grid[0])

        def dp(i, j):  # return min sum of paths
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[0][0]

            res = min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]

            memo[(i, j)] = res
            return res

        return dp(m - 1, n - 1)


'''
DP table and 2 dimension DP
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or grid == [[]]:  # corner case
            return 0

        m, n = len(grid), len(grid[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[m][n]
