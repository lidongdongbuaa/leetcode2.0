#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 15:24
# @Author  : LI Dongdong
# @FileName: 33. Search in Rotated Sorted Array.py
''''''
'''
题目分析
find the target value in the sorted rotated array, return its index, else return -1
O(logN)
binary search problem

input: nums:list[int], repeated value in it? N; ordered, Y; len(nums) range? [1, 10000]; value range? [-2*32, 2*32]
output:int or -1
corner case: 
    nums is None? Y -> -1
    nums is only one? Y -> as request
    target is None? Y -> -1

5.方法及方法分析：brute force; binary search
time complexity order: binary search O(logN) < brute force O(N)
space complexity order: O(1)
6.如何考
'''
'''
A.brute force - traversal all value
    Method:
        traversal all elements in nums, and check the target, if having, return True, else return False
    time complexity: O(N)
    space complexity: O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if target == value:
                return index
        return -1

'''
B. binary search for target
    Method:
        1. set left bonderay, l, as 0; set right bondery, r, as len(nums) - 1
        2. do while loop, l <= r
            a. mid = 1 + (r - l)//2
            b. case1: target == nums[mid], return mid
            c. case2: left part is sorted
                case 2.1 nums[l] < target < nums[mid]  ->r = mid - 1
                case 2.2 else l = mid + 1
            d. case3: right part is sorted
                case 3.1 nums[mid] < target < nums[r] -> l = mid + 1
                case 3.2 else -> r = mid - 1
        3. return -1
    time complexity O(logN)
    space complexity O(1)
易错点：两种情况的话，第一种情况先满区间，后一个直接else
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  # corner case
            return -1
        if target is None:
            return -1

        if len(nums) == 1:
            if target in nums:
                return 0
            else:
                return -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1