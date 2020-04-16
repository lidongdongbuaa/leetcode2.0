#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 15:24
# @Author  : LI Dongdong
# @FileName: 11. Container With Most Water.py
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
input: height, list; length rang is from 2 to inf; vlaue range, no limit; have repeated value; no order
output: int
corner case
    lenght of height is 2, return min (two elem)

A. brute force - scan every value and calculate all kinds containing
    Method:
        1. scan elem i in height
            scan other right elems j
                calculate the containing
                renew the max containing
    Time complexity: O(n^2)
    Space: O(1)

'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)

        res = 0
        n = len(height)
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res
