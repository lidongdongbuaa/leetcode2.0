#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 11:18
# @Author  : LI Dongdong
# @FileName: 81. Search in Rotated Sorted Array II.py
''''''
'''
题目概述：在rotated sorted array里面找目标值
题目考点： 在分块后，块可能不是sorted的，出现头值l和尾值mid重复，怎么处理
解决方案： 不断缩进left part的left边界，直到l不等于mid，此时left块是sorted，再进行binary search
方法及方法分析：brute force, binary search
time complexity order: binary search, worst O(N) = brute force O(N)
space complexity order: O(1)
如何考
'''
'''
find value in a repeated value sorted rotated array

input: 
    nums, list; length rang of list? [0,+1000]; value range? [-10000, 1000]; repeated? Y
    target, int: None? Y; out of range of nums? Y
output:
    True, find the target
    False

A. brute force - scan one by one
    Time complexity: O(N)
    Space: O(1)

B. binary search, first set then do
    Method:
        1. corner case
        2. transfer list as set to remove repeated values, then transfer as list
        3. find the target in list by binary search
            a. divide by mid
            b. find the target, in sorted part and in unsorted parted
    Time: O(N)
    space： O(N)

corner case: Nums is None, target is None

C. Method:
    1. corner case
    2. set left and right boundary; 
    3. do while loop and use mid to divide the nums into left and right part
        if find, return True
        if left part's head = tail, traversal left boundary to make the left part sorted
        if left part is sorted, check target in left or right part, then scale the boundary
        if right part is sorted, do the same thing

    Time complexity: worst O(N) [1,1,1,1...]
    Space: O(1)
易错点：
    1. 一定要对着method写代码，不要漏
    2. r - l顺序不要弄反了
    3. nums[mid] = target不要漏
    4. if elif else是并列关系，不要ififelse!
'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums is None:  # corner case
            return False
        if target is None:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:
                l += 1
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
