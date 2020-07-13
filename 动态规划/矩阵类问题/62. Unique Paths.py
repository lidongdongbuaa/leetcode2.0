#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 8:57
# @Author  : LI Dongdong
# @FileName: 62. Unique Paths.py
''''''
'''
题目概述：求从左上到右下的所有路径，只有两个方向，右和下
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input:
    m is columns, value range is 1 to 100
    n is rows, value range is 1 to 100
output: int, the number of unique path
corner case:
    m = n = 1, return 1


超时
A. backtrack - dfs
    Method:
        1. create a visited tag list
        2. from start to dfs scan the grid, only right and down way
            if reach to finish point, save path in set
        3. return set length

    Time complexity: O(2^(nm))
    Space: O(m + n)
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:  # corner case
            return 1

        visited = [[0] * m for _ in range(n)]

        res = []

        def dfs(i, j, path):  # save path in res
            if i < 0 or j < 0 or i > n - 1 or j > m - 1 or visited[i][j] == 1:
                return

            path.append([i, j])
            visited[i][j] = 1

            if i == n - 1 and j == m - 1:
                res.append(path[:])
            for (x, y) in ((i + 1, j), (i, j + 1)):
                dfs(x, y, visited)

            visited[i][j] = 0
            path.pop()

        dfs(0, 0, [])
        return len(res)


'''

B. DP - dp(i, j) is the number of path when reach to (i,j) point in grid
    Method:
        1. set memo dict to save the (i, j) and dp value 
        2. function: dp(i,j) = dp(i - 1, j) + dp(i, j - 1)
        3. base case: i = 0, j = 0, return 1; if i < 0, or j < 0, return 0
    Time complexity: O(n * m)
    Space： O(n * m)

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:  # corner case
            return 1

        memo = {}

        def dp(i, j):  # return number of path reaching to (i,j)
            if (i, j) in memo:
                return memo[(i, j)]

            if i == 0 or j == 0:
                return 1

            res = dp(i - 1, j) + dp(i, j - 1)
            memo[(i, j)] = res
            return res

        return dp(n - 1, m - 1)


'''
DP table
增加空层，base case与memo法一致
'''

'''
dp 
dp(i, j) = dp(i - 1, j) + dp(i, j - 1)

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if r == 1 or c == 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]