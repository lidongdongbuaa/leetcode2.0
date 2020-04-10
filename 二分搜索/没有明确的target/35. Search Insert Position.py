#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 16:49
# @Author  : LI Dongdong
# @FileName: 35. Search Insert Position.py
''''''
'''
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    
    You may assume no duplicates in the array.
    
    Example 1:
    
    Input: [1,3,5,6], 5
    Output: 2
    Example 2:
    
    Input: [1,3,5,6], 2
    Output: 1
    Example 3:
    
    Input: [1,3,5,6], 7
    Output: 4
    Example 4:
    
    Input: [1,3,5,6], 0
    Output: 0
题目分析 - 找有可能不存在的target的位置, 返回L的情况
search numb in arr, return the index of it or its possible position
array binary search

input: arr[int, ...]; val is repeated? N; arr is ordered? Y; target is int
output: int of index
corner case:
    1. arr is None? Y -> 0
    2. arr has only one elem? Y
    3. target is NOne? Y -> 0
    4. target is out of range of arr? Y
    
方法及方法分析：brute force - two pointer; binary search
time complexity order: binary search O(logN) < brute force - two pointer O(N)
space complexity order: O(1)
6.如何考
'''
'''
A brute force - two pointer and compare
    Method:
        1. corner case, out of range, only one
        2. traversal arr elements,i index, from 0 to len(arr) - 1
            if arr[i] == target, return i
            if arr[i + 1] == target, return i + 1
            if arr[i] < target < arr[i + 1], return i + 1
    Time complexity: O(N)
    Space complexity: O(1)
易错点：
    处理好只有一个值的情况
    看到(len(nums) - 1)，就该处理1个值的情况
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:  # corner case
            return 0
        if target is None:
            return 0

        if target <= nums[0]:
            return 0
        if nums[-1] < target:
            return len(nums)

        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            if nums[i + 1] == target:
                return i + 1
            if nums[i] < target < nums[i + 1]:
                return i + 1
'''
B binary search
    Method:
        1. corner case
        2. set left boundary, l, as 0; right boundary, r, as len(arr) - 1
        3. do while loop
            a. set the mid = l + (r - l)//2
            b. if arr[mid] = target, return mid
            c. if arr[mid] < targer, change left boudary
            d. if arr[mid] > target, change right boudary
        4. return l as result which is the smallest bigger value to target
    Time complexity: O(logN)
    Space: O(1)
    改进：(r - l) // 2 -> (r -l) >> 1
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            if target > nums[mid]:
                l = mid + 1
        return l