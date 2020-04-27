#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 15:19
# @Author  : LI Dongdong
# @FileName: 455. Assign Cookies.py
''''''
'''
题目概述：给定两个list，一个是需求list，一个是可满足list，问多少个需求可以被满足
题目考点：greedy，先满足一个，再满足下一个
解决方案：greedy + 分离双指针
方法及方法分析：
time complexity order: O(mlogm + nlogn)
space complexity order: O(1)
如何考
'''
'''
input: 
    g, child need; list; length range is from 0 to inf; value range is from 0 to inf; have repeateed; no order
    s, cookies; length range is from 0 to inf; value range is from 0 to inf; have repeated; no order
output:
    int; the number of children content
corner case
    g is None, return 0
    s is None, return 0

A. Greedy
    Method:
        1. sort g and s
        2. two seperate pointer to scan g by i, scan s by j
            if s[j] >= g[i]; i += 1, j += 1
            else: j += 1
        3. return i + 1
    Time complexity: O(mlogm + nlogn)
    Space: O(1)

'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g:  # corner case
            return 0
        if not s:
            return 0

        g.sort()
        s.sort()

        m = len(g)
        n = len(s)
        i = j = 0

        while i < m and j < n:
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i

