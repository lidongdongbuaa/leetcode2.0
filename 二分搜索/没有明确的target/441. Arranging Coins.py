#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 9:22
# @Author  : LI Dongdong
# @FileName: 441. Arranging Coins.py
''''''
'''
题目目的概述: 给出n，问多少层递加1的阶梯可以构成 -> 在一列数[1,x]中，对于要求n，找到i可以满足(i+1)*i//2= n，若i不存在，则的i最大值
方法及方法分析： brute force - accumulate values； binary search
time complexity order: binary search O(logN) < brute force - accumulate values O(N)
space complexity order: O(1)
如何考
'''
'''
count the numbers of rows we can make by n coins


input: number of coins, int; None? N; only one? Y; 0? Y
output: int

A.brute force - accumulate values
    Method:
        1. corner case - only one
        2.accumulate value i, from 1 to n as sumNum
                if sumNum > n, i - 1 is result, return i

        Time complexity: O(N)
        Space: O(1)

'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:  # corner case
            return 1
        if n == 0:
            return 0

        sumNum = 0
        for i in range(1, n + 1):
            sumNum += i
            if sumNum > n:
                return i - 1


'''


B. binary search
    Method:
        1. corner case
        2. sum of coins = (row index, i) * (row index + 1) // 2
            find i can make sum of i >= n by binary search in sequence [1, n]
            a. l, r boundary as 1, n
            b. do while loop, l <= r
                mid  = l + (r - l) // 2
                if sum of mid (by the equation) == n:return mid
                if sum of mid < n, l = mid + 1
                if sum of mid > n, r = mid - 1
            c. not find mid, return r

        Time complexity: O(logN)
        Space: O(1)

n = 5

l, r = 1, 5
loop1:
    mid = 3
    sum = 6 > n = 5
    r = mid - 1 = 2
loop2:
    l,r = 1, 2
    mid = 1
    sum = 1
    l = mid + 1 = 2
loop3
    l, r= 2, 2
    mid = 2
    sum = 3 < n
    l = 2 + 1 = 3
loop 4
    return 2

'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:  # corner case
            return 1

        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            if total < n:
                l = mid + 1
            else:
                r = mid - 1
        return r

