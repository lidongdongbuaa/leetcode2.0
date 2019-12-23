#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 8:28
# @Author  : LI Dongdong
# @FileName: 516. Longest Palindromic Subsequence.py
''''''
'''
https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/
1.要求：Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
    Example 1:Input: "bbbab" Output: 4 One possible longest palindromic subsequence is "bbbb".
    Example 2: Input: "cbbd" Output: 2 One possible longest palindromic subsequence is "bb".
2.理解：寻找最长的，可以不连续，但有序的子序列，满足是回文要求
3.类型：string
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:None? Y One? Y repeat? Y order? N
    output: 0/1...int
    focus on time or space? space
'''

'''
idea：DFS + judge/record
Method：
    use DFS to get all possible subsequence  # tO(2^N) sO(N)
    judge whether the subseq is the palindromic using hash table # tO(N) sO(N)
time complex: 
space complex: 
易错点：
'''