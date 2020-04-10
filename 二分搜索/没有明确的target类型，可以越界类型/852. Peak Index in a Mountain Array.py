#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:25
# @Author  : LI Dongdong
# @FileName: 852. Peak Index in a Mountain Array.py
''''''
'''
题目目的概述: 一列数，前半段上升，后半段下降，找出峰值点
方法及方法分析：traversal compare; linear search drop; binary search
time complexity order:  binary search O(logN) < traversal compare O(N) =  linear search drop O(N)
space complexity order:  O(1)
如何考
'''
'''
find an array's mountain peak's index

input:A:list, number of A [3, 10000]; value range of A elem? [0, 10000]; A elem has repeat? N; has order? Y, ascedning + descending
output: int
corner case:
    A is None? N
    A is only one? N

find the biggest value's index in anarray 

A.traversal and compare to find the biggest value
    Method:
        1. set res = 0
        2. traversal all node, res = max(res, i node)
        3. return the res
    Time complexity: O(N)
    Space: O(1)

'''


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:  # corner case
            return None

        res = 0
        for i in A:
            res = max(i, res)
        return res


'''
B. linear search
     the peak is where the elem stops increaseing
    Time complexity: O(N)
    Space: O(1)
'''


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:  # corner case
            return None

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return i


'''
sorted array in part
binary search
B. binary search 
    Method:
        1. set left boundary index, l, and right bounderay index, r
        2. do while loop, l + 1 < r
            find mid index
            if nums[mid] < nums[mid + 1]
                l = mid
            if nums[mid] > nums[mid + 1]
                r = mid
        3. return max value's index

    Time complexity: O(logN)
    Space: O(1)
'''


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:  # corner case
            return None

        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if A[mid] < A[mid + 1]:
                l = mid
            else:
                r = mid
        if A[l] < A[r]:
            return r
        else:
            return l


'''
test case

index  0, 1, 2
      [0, 1, 0]

pass corner case
l, r = 0, 2
loop1:
    mid = 1
    nums[mid] = 1, nums[mid + 1] = nums[2] = 0
    r = 1
loop 2:
    l = 0, r = 1
    return 
 nums[l] = 0, nums[r] = 1
 return r = 1

'''