#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 15:19
# @Author  : LI Dongdong
# @FileName: 459. Closest Number in Sorted 数组 (Lintcode).py
''''''
'''
    Description
    Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.
    
    Return -1 if there is no element in the array.
    
    Notice
    There can be duplicate elements in the array, and we can return any of the indices with same value.
    
    
    
    Example
    Given [1, 2, 3] and target = 2, return 1.
    
    Given [1, 4, 6] and target = 3, return 1.
    
    Given [1, 4, 6] and target = 5, return 1 or 2.
    
    Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: 
    list, [int]; length range? [0, +100000]; value range? [-1000, +10000]; repeated? Y; order? Y
    target: int; value range? as list; None? Y
output: index, int
corner case: 
    list is None? -> return -1
    target is None? -> return -1

A. brute force - compare one by one
    Method:
        1. corner case
        2. compare target with elem i of nums one by one, 
            if elem is bigger than target, compare i with i - 1 to choose the smallest one to output
    Time complexity: O(N)
    Space: O(1)

B. binary search
    Method:
        1. corner case
        2. set left and right boundary
        3. do while loop, use mid to divide the nums until find the target, return index
            or l > r, return closest one
    Time complexity: O(logn)
    space: O(1)
'''
class Arr:
    def findClosestIndex(self, nums, target):  # return the closest index
        if not nums:  # corner case
            return -1
        if target is None:
            return -1

        if target <= nums[0]:
            return 0

        if target >= nums[-1]:
            return len(nums) - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if abs(nums[l] - target) < abs(nums[r] - target):
            return l
        else:
            return r
