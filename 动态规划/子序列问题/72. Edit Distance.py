#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 12:29
# @Author  : LI Dongdong
# @FileName: 72. Edit Distance.py
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
find the operation numbers

input: two string; length range? from 0 to inf; string letter is uppercase or lowercase letter? any one is ok; repeated? y; order? No
output: int; if same, return 0
corner case: 
    word1 == word2, return 0
    word1 or word2 is None? return others length

A. brute force - dp recursion from end to start of string
    Method:
        1. corner case
        2. dp(i,j): the shorest edit times of s1[0...i] with s2[0...j]
        3. if s1[i] == s2[j], not add times , return dp(i, j)
            else:
                dp(i, j) = insert/ delete / replace times (=1) + dp(new i, new j)
        4. return dp(m-1, n-1), m i s len of word1, n is len of word2
    Time complexity :O((3^max(m, n)) 递归树节点的总数 * 每个节点的操作时间
    Space: O((max(m, n)) Height of the recursion stack

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:  # corner case
            return 0

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        def dp(i, j):  # return distance of w1[0:i] with w2[0:j], transfer w1 to w2
            if i == -1:  # i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度。
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                delete = dp(i - 1, j) + 1
                insert = dp(i, j - 1) + 1
                replace = dp(i - 1, j - 1) + 1
                return min(delete, insert, replace)

        return dp(len(word1) - 1, len(word2) - 1)


'''
B. dp with memo - use a memo to save the dp[i][j] value
    Time complexity: O(m * n)
    Space :O(m * n)
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:  # corner case
            return 0

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        memo = {}

        def dp(i, j):  # return edit times to w1[i] and w2[j]
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = 1 + min(dp(i - 1, j - 1), dp(i - 1, j), dp(i, j - 1))
                return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)