#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 16:03
# @Author  : LI Dongdong
# @FileName: 153. Find Minimum in Rotated Sorted Array.py
''''''
'''
题目目的概述。 找rotated sorted list里的最小值
方法及方法分析：brute force - traveral, binary search
time complexity order: binary search O(logN) < brute force O(N)
space complexity order: O(1)
如何考
'''
'''
have a array, find its minimum value, array is rotated sorted
[1,2,3,4,5] - > [3,4,5,1,2]


input: arr: list[int]
output:min value: int
corner case：
    arr is None? Y -> None
    arr is only one number? Y -> this numb

A brute force - traversal every one, and find the min one
    Method:
        1. corner case
        2. set res = nums[0]
        3. traversal nums [1, len(nums)] to renew the res
        4. return the res
    Time complexity : O(N)
    Space: O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return None
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        for i in nums:
            res = min(res, i)
        return res
''''
sorted rotated array - binary search

B. binary search - judge the sorted part, 最小值一定在unsorted part
    Method:
        1. corner case
        2. set left bondary,l, by 0, set right boundary, r, as len(nums) - 1
        3. do while loop, i <= r
            mid = l + (r - l) // 2
            if left part and right part is ordered(=): return nums[l]
            if left part is sorted and right is not: change l as mid + 1
            if right part is sorted and left is not: change r as mid - 1
    Time complexity: O(logN)
    Space: O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return None
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
            if nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                l = mid + 1  # 肯定不在mid上，所以mid + 1
            else:
                r = mid
'''
test case
 0,1,2,3,4
[3,4,5,1,2] 
pass corner case
l, r = 0, 4
loop1:
    mid = 2
    n[l] = 3, n[mid] = 5, n[r] = 2
    l = 3
loop2:
    l = 3, r = 4
    mid = 3
    n[l] = 1, n[mid] = 1, n[r] = 2
    return num[l] = 1

 0,1,2,3,4,5,6
[4,5,6,7,0,1,2]
pass corner case

l,r= 0, 6
loop1:
    mid = 3
    n[l], n[mid], n[r] = 4, 7, 2
    l = 4
loop2:
    l = 4, r= 6, mid = 5
    n[l] = 0, n[mid] = 1. n[mid] = 2
    return n[l] = 0


 0, 1, 2
[3, 1, 2]
l = 0, r = 2
loop1:
    mid = 1
    n[l] = 3, n[mid] = 1, n[r] = 2
    r = 0
'''
'''
C.模板解法
易错点: 划分区间时,无论左区间是有序的,还是无序的,最小值有可能在此左区间,故不能用左区间两端点来划分区间
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return None
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[r] < nums[mid]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])