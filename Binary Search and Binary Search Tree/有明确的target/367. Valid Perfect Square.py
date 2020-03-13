#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 11:19
# @Author  : LI Dongdong
# @FileName: 367. Valid Perfect Square.py
''''''
'''
题目分析
1.要求：Given a positive integer num, write a function which returns True if num is a perfect square else False.

    Note: Do not use any built-in library function such as sqrt.
    
    Example 1:
    
    Input: 16
    Output: true
    Example 2:
    
    Input: 14
    Output: false 
2.理解： find a number which could square as the given num
3.类型： search problem
4.确认输入输出及边界条件：
    input: int, num range? [1, 100000]
    output: T/F
    corner case: 
        num <= 0? N
        num would be 1? Y -> T
        num is None? N
5.方法及方法分析：Brute force; binary search; Newton Method
time complexity order: binary search O(logN) = Newton Method O(logN) < Brute force O(N)
space complexity order: O(1)
6.如何考
'''
'''
A. Brute force
    Method:
        1. traversal number from 1 to half of num to check if the number * number is num
            if true, return true
            else return False
    time complexity: O(n)
    space : O(1)
易错点：
'''


class Num:
    def isSqare(self, num):  # return True of square num, else return Faslse
        if num == 1:  # corner case
            return 1

        for i in range(1, num // 2):
            if i * i == num:
                return True
        return False


'''
B. binary search the result from 1 to half of num
    Method:
        1. set left  boundary, l, as 1,  set right boundary,r, as num//2
        2. do while traversal, l <= r
            a. mid = (l + r)//2
            b. check if the mid^2 == num?
                return True
            c. mid^2 < num
                l = mid + 1
            d. mid^2 > num
                r = mid - 1
    time O(logN)
    space O(1)
'''


class Num:
    def isSquare(self, num: int):  # return True if num is perfect square, False for no prefect square
        if num == 1:
            return True

        l = 1
        r = num // 2

        while l <= r:
            mid = (l + r) // 2
            tmp = mid * mid
            if tmp == num:
                return True
            elif tmp < num:
                l = mid + 1
            elif tmp > num:
                r = mid - 1
        return False


'''
test code
input: 16
l:1, r：8
loop1:
    mid = 4
    tmp = 16
    tmp == num -> return True

input: 14 = num
l:1, r: 7
loop1:
    mid = 4
    tmp = 16
    tmp > num
        r = 3
loop2:
    mid = 2
    tmp = 4 < num
    l = 2 + 1 = 3
loop3
    mid = 3
    tmp = 9 < num
        l = mid + 1 = 4
    out of loop
return False
'''
'''
C.Newton 
time O(logN)
space O(1)
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
