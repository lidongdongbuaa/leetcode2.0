#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 10:18
# @Author  : LI Dongdong
# @FileName: 1143. Longest Common Subsequence.py
''''''
'''
题目概述：求两列字符串的最长公共子序列
题目考点：回溯；二维双字符串dp
解决方案：回溯求全部；dp[i][j] = dp[i-1][j-1] + 1
方法及方法分析：回溯；dp
time complexity order: 回溯 O(2^(m + n)) > dp O(m * n) 
space complexity order: 回溯 O(2^m + 2^n) > dp O(m * n) 
如何考
'''
'''
find longest common subsequence

intput:
    text1,text2, string; length range? from 0 to 10000; character format,uppercase or lowercase? lower case;repeated? Y; order? N
output:
    int; else, 0
corner case:
    text1 or text2 is None? return 0

A. brute force - find all sequence of  text1 and text2 by backtracking, and compare
    Time: O(2^n + 2^m + 2^m * 2^n), n, m is the length of text1 and text2
    Space: O(2^m + 2^n)

B. DP method - dp[i][j] is the longest common sequence with text1 * text2 matrix [i][j]
    Method:
        1. corner case
        2.  
            a. dp[i][j]: 扫描到text1[i- 1]和text2[j-1]时的最长公共子序列
            b. if nums[i] = nums[j],  dp[i][j] = dp[i][j] + 1
                else: dp[i][j] = max(dp[i][j-1,..0], dp[i-1,...][j])
            c. base case, dp[i][j] = 0
    Time O(m *n)
    Space: O(m*n)
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 第一行，第一列都为空

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # 从i-1,j-1累加，即dp[i-1][j-1]是完全不包含ij的最长，dp[i][j]是完全包含ij的最长
                    # [i][j-1]或[i-1][j]是半包含ij的最长，半包含最长可能等于全包含最长，故不能是dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]


'''
input: 
    text1, text2, string, lenght range is from 0 to 1000, only character? Y
output:
    int, number of common subsequence length

brute force - find all substring of text1 and text 2 and compare
time complexity: 2^n + 2n = 2^n, n is max length of text1 and text2
space complexity: 2^n * 2

dp
dp[i][j] - longest length of subsequence when reaching to text1[i] and text2[j]
for loop i range 0 to n - 1
    for loop j range 0 to m - 1
        if text1[i] == text2[j], dp[i][j] = dp[i - 1][j  - 1] + 1
        else: dp[i][j] = max(dp[i - 1][j - 1], dp[i][j-1], dp[i - 1][j])
base case:
    i = 0 and j =0, if text1[i] == text2[j], dp[0][0] = 1, else 0
    i = 0, dp[i][j]= 0
    j = 0, dp[i][j]= 0
return dp[n - 1][m - 1]
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # corner case
        if not text1 or not text2:
            return 0

        t1 = text1
        t2 = text2

        # dp
        m = len(t1)
        n = len(t2)

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if t1[i] == t2[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif i == 0:
                    if t1[i] == t2[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if t1[i] == t2[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if t1[i] == t2[j]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]

'''
dp with padding
边界状态值的确定需要考虑多种情况时，用padding
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # corner case
        if not text1 or not text2:
            return 0

        t1 = text1
        t2 = text2

        # dp
        m = len(t1)
        n = len(t2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t1[i - 1] == t2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]