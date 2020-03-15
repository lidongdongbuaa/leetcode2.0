#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 10:22
# @Author  : LI Dongdong
# @FileName: 69. Sqrt(x).py
''''''
'''
题目目的概述 找一个数的平方根，若不为整数，取整数部分 -》 在一列数[1,n+1]中，找到最大数i可以让i^2 <= n，i在假设值的左侧，故取r
方法及方法分析：brute force - scan and choose， binary search, Pocket Calculator Algorithm
time complexity order: Pocket Calculator Algorithm O(1) < binary search O(logN) < brute force - scan and choose o(N)
space complexity order: O(1)
如何考
'''
'''
calculate the square root of x and return the integet part

input: x, int; range of int? [0, +10000]
output: int

A. brute force - scan and choose
    Method:
        1. corner case, x is 1
        2. traversal i from 1 to x
            if i^2 > x, return i - 1
    input: 4
    i = 1, 2,3, return 2
    input 8
    i = 1,2,3, return 2

    Time complexity: O(N)
    Space:  O(1)
易错点：考虑到x为0时
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  # corner case
            return 0
        if x == 1:
            return 1

        for i in range(1, x + 1):
            if i * i > x:
                return i - 1


'''
B. binary search to find i, i is the biggest value which i ^ 2 <= input x
    Method:
        1. corner case
        2. l, r = 1, x
        3. do while loop, l <= r
            mid = l + (r - l) // 2
            if mid^2 == x
                return mid
            if mid^2 < x:
                l = mid + 1
            else:
                r = mid - 1
        4. if not find mid, return r

    time complexity: O(logN)
    space: O(1)

    input: 4
    l,r = 1, 4
    loop1:
        mid = 2
        mid^2 = 4 = x
        return 2

    input: 8
    l, r = 1,8
    loop1:
        mid = 4
        mid^2 = 16 > x = 8
        r = 3
    loop 2:
        l, r = 1, 3
        mid = 2
        mid^2 = 4 < x = 8
        l = 2
    loop 3
        l, r = 2, 3
        mid = 2
        mid^2 = 4 < x = 8
        l = 3
    loop 4
        l, r = 3,3
        mid = 3
        mid^2 = 9 > 8
        r = 2
    loop5
        l, r = 3, 2
        return 2


'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:  # corner case
            return 1

        l, r = 1, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

'''
Pocket Calculator Algorithm
x = e^logx -> x^1/2 = e^(1/2 * logx)
'''
from math import e, log


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right