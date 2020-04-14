#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 10:19
# @Author  : LI Dongdong
# @FileName: 221. Maximal Square.py
''''''
'''
题目概述：本题做错了，要回头看一下
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
dp[i][j] is the max edge lenght of square inclusing i, j cell
    dp(i,j) =  min(dp(i - 1, j), dp(i - 1, j - 1), dp(i, j - 1)) + 1
    base case:
         i or j < 0, return float('-inf')
         i = j = 0, if matrix[i][j] = 1, return 1
            else, return 0

'''


class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or matrix == [[]]:  # corner case
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dp(i, j):  # return largest area
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0:
                return float('-inf')

            if (i == 0 or j == 0) and matrix[i][j] == '1':
                res = 1
            elif (i == 0 or j == 0) and matrix[i][j] == '0':
                res = float('-inf')

            elif matrix[i][j] == '1':
                res = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1
            else:
                res = dp(i - 1, j - 1)
            memo[(i, j)] = res
            return res

        dp(m - 1, n - 1)
        maxLength = 0
        for l in memo.values():
            if l != float('inf'):
                maxLength = max(maxLength, l)
        return maxLength * maxLength


'''
有问题，回头看
'''
'''
dp[i][j] is the max edge lenght of square inclusing i, j cell
    dp(i,j) =  min(dp(i - 1, j), dp(i - 1, j - 1), dp(i, j - 1)) + 1
    base case:
         i or j < 0, return float('-inf')
         i = j = 0, if matrix[i][j] = 1, return 1
            else, return 0

'''


class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or matrix == [[]]:  # corner case
            return 0

        m, n = len(matrix), len(matrix[0])

        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        maxLength = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    if matrix[i - 1][j - 1] == '1':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = float('-inf')
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

                if dp[i][j] != float('-inf'):
                    maxLength = max(maxLength, dp[i][j])

        return maxLength * maxLength
