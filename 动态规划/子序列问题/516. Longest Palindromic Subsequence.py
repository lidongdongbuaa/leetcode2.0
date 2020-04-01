#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 16:33
# @Author  : LI Dongdong
# @FileName: 516. Longest Palindromic Subsequence.py
''''''
'''
题目概述：求最长回文子序列长度
题目考点：回溯；dp
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
longest palindromic subsequence

input: string; length range? from 0 to 1000; the letter uppercase or lowercase? lowercase;
output:int; if no, 0
corner case: s is None, return 0

A.brute force - get all sequence and check if it is palindromic, and count
Time :(2^n * n), n is len(s)
Space: (2^n)
'''
from copy import deepcopy


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:  # inp:string, outp:int, find longestSubseq
        if len(s) == 0:  # edge case
            return 0
        if len(s) == 1:  # edge case
            return 1

        def backtrack(start, path):  # return all subsequnce
            allSeq.append(''.join(path))

            for i in range(start, len(s)):
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()

        allSeq = []
        backtrack(0, [])  # store all possible subsequence
        all_subseq = allSeq

        length = 0
        for elem in all_subseq:  # judge whether is palindromic and record its longest length
            if self.judge(elem):
                length = max(length, len(elem))
            else:
                pass
        return length

    def judge(self, S):  # judge whether S is palindromic
        if len(S) == 1:  # edge case
            return True

        for i in range(len(S) // 2):
            if S[i] != S[-(i + 1)]:
                return False
        return True


'''
B. brute force DP - dp(i, j) the longest palindromic subseq in s[i:j]
    Method:
        1. corner case
        2. if s[i] = s[j], dp(i,j) = dp(i - 1,j + 1) + 2, else, dp(i, j) = max(dp(i - 1,j), dp(i, j + 1))
    Time complexity: O(2^n)
    Space:  O(2^n)
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        def dp(i, j):  # return the longest palincdromic subseq in s[i:j + 1]
            if i == j:
                return 1
            if i > j:
                return 0

            if s[i] == s[j]:
                return dp(i+ 1, j - 1) + 2
            else:
                return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, len(s) - 1)


'''
C. optimized DP - DP table
    Method:
        1. corner case
        2. use dp[][] to save the dp[i][j] values
        3. base case 
            dp[i][i] = 1

遍历的方向问题：
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


'''
D. optimized DP - DP memo
    Method:

'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        memo = {}

        def dp(i, j):  # return the longest palincdromic subseq in s[i:j + 1]
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                memo[(i, j)] = 1
                return 1
            if i > j:
                memo[(i, j)] = 0
                return 0

            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1) + 2
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j - 1))
            return memo[(i, j)]

        return dp(0, len(s) - 1)