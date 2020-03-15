#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 20:09
# @Author  : LI Dongdong
# @FileName: 278. First Bad Version.py
''''''
'''
题目目的概述 一系列version，从前往后1->n, 从i开始bad，有isBadVersion判断，求那个开始坏了
方法及方法分析： brute force - try one by one;  binary search
time complexity order:  binary search O(logN) < brute force - try one by one O(N)
space complexity order: O(1)
如何考
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

'''
find the beginning bad at a sorted array

input: n:int
output: int
corner case: 
    n is None? N
    n is 0? -> N
    n is 1? -> return as rule
    we must have bad? Y

A. brute force - try one by one
    Method:
        traversal every version from 1 to n
            check if it is bad, Yes, return index

    Time complexity: O(N)
    Space: O(1)

'''


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i


'''

B. binary search
    Method:
        1. set left and right boundary
        2. do while loop, l <= r
            mid = l + (r - l) // 2
            if mid is bad:
                r = mid - 1  # 设想要求的是bad的左边的第一个数
            if mid is Good:
                l = mid + 1
        3. return l

n = 5, and version = 4
    l = 1, r = 5
    loop1:
        mid = 3
        mid is good
        l = 4
    loop2
        l,r = 4, 5
        mid = 4
        mid is bad
        r = 3
    loop3
        l, r = 4, 3
        return 4
易错点：题目的要求可以转化为求i的右值（i是最后一个good的version），所以把边界条件按照求i来定义
'''


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
