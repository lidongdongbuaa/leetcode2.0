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
input: matrix, list[list]; length range is from 0 to inf; value is only 0 or 1
output:int, the area of the square
corner case:
    1. matrix is None, return 0

A. DP - dp[i][j] is the longest length of the edge of the square with right bottom point (i, j)
    Method:
        1. corner case
        2. dp(i,j) =  min(dp(i - 1, j), dp(i - 1, j - 1), dp(i, j - 1)) + 1
        3. base case:
            a. for i in range (1, m + 1)
            b. dp = [float('inf')]
            c. meet '0', dp = [float('inf')]
'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or matrix == [[]]:  # corner case
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        length = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    if i == 1 or j == 1:  # 包含了原点和边
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    length = max(dp[i][j], length)
        return length * length

'''
这种跳值的，即matrix[i - 1][j - 1] == 0,时，dp[i][j]直接为0的情况下，无法进行dp memo方法，
总结就是 若除了base case，若dp只能用dp的sub的情况表示时，可以用dp memo，否则只能用dp table
'''