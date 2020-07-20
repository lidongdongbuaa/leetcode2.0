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

input:matrix; length range is from 0 to inf; vlaue is 0 or 1;
output: int, the number of path
corner case:
    matrix is None; return 0
    only one cell, matrix[0][0] == 1, return 0 else 1

A.DP - dp(i, j) is the ways number when reaching to matrix[i][j]
    Method:
        1. dp(i, j) = dp(i - 1, j) + dp(i, j - 1)
        2. base case
            if i == 0 and matrix[i][0] = 1, return 0
                matrix[i][0]= 0, return 1
            if j == 0 and matrix[0][j] = 1, return 0
                matrix[0][j] = 0, return 1
            if matrix[i][j] = 1, return 0
        3. return dp(len(matrix) -1 , len(matrix[0] - 1))
    Time complexity: O(m * n)
    Space: O(m + n)

'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        if not grid:  # corner case
            return 0

        memo = {}
        m = len(grid)
        n = len(grid[0])

        def dp(i, j):  # return number when reaching to i, j cell
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0 and grid[i][j] == 1:
                return 0
            if i == 0 and j == 0 and grid[i][j] == 0:
                return 1
            if grid[i][j] == 1:
                return 0


            res = dp(i - 1, j) + dp(i, j - 1)
            memo[(i, j)] = res
            return res

        return dp(m - 1, n - 1)


'''
DP Table
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m = len(grid)
        n = len(grid[0])

        if not grid or grid == [[]]:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if r == 1 and c == 1:
                    if grid[r - 1][c - 1] == 1:
                        return 0
                    else:
                        dp[r][c] = 1
                else:
                    if grid[r - 1][c - 1] == 1:
                        dp[r][c] = 0
                    else:
                        dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]
