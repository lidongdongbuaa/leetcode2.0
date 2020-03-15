#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 15:24
# @Author  : LI Dongdong
# @FileName: 33. Search in Rotated Sorted Array.py
''''''
'''
题目分析 - 本题重点看
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
A. Binary search
    Method:
        1. corner case
        2. set left and right boundary
        3. do while loop
            a. set mid
            b. if arr[mid] == target, return mid
            c. if l part is sorted, move boundary
            d. if r part is sorted, move boudnary

        Time complexity: O(logN)
        Space: O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  # corner case
            return -1


        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            if nums[l] < nums[mid]:  # 判断左边有序
                if nums[l] <= target < nums[mid]:  # 因为此时target != nums[mid]
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] == nums[mid]:  # 左边与mid相等
                l = mid + 1
            elif nums[l] > nums[mid]:  # 右边有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1




