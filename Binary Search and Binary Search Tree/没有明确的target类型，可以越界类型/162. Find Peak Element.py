#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 11:55
# @Author  : LI Dongdong
# @FileName: 162. Find Peak Element.py
''''''
'''
题目目的概述：找一列值中的peak峰值点，最左侧和最右侧点都包含
方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
find the biggest val among its neighbors, return the index of it

input: nums:[int], value range? [-infinite, infinite]
output: any index of the peak value
corner case:
    num is None? Y -> -1
    num is Only one? Y -> num[0]
    num is only two? Y -> max(nums[0], nums[1])'s index
    nums is only three?

思路不对，少考虑peeak在边界上的情况
A. brute force - traversal and compare
    Method:
        1. corner case
        2. scan elem i from 0 to len(num) - 2
            if nums[i] < nums[i + 1] and nums[i + 2] < nums[i + 1], return i + 1
        3. return -1
    Time complexity: O(N)
    Space complexity: O(1)
易错点：
    是nums[i] < nums[i + 1] and nums[i + 2] < nums[i + 1]， 不是nums[i] < nums[i + 1]< nums[i + 2]
    len(nums) == 1时，返回的是 index = 0,不是值
    这个peak的概念，1,0,1，第一个1也是peak
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums is None:  # corner case
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 1
            else:
                return 0
        if len(nums) == 3:
            if nums[0] > nums[1]:
                return 0
            if nums[1] > max(nums[0], nums[2]):
                return 1
            if nums[2] > nums[1]:
                return 2


        for i in range(len(nums) -2):
            if nums[i] < nums[i + 1] and nums[i + 2] < nums[i + 1]:
                return i + 1
        return -1

'''
A. liner scan - peak一定在下降区间的第一个
    Method:
        case 1. ascending arr
            num[i] < num[i + 1], pass
            so return len(num) - 1
        case 2. descending arr
            num[i] > nums[i + 1]
            so return i
        case 3. ascending arr, then deseceding arr
            when num[i] > nums[i + 1]
            return i
    Time complexity: O(N)
    Space: O(1)
    易错点：注意前提条件，nums[i] != nums[i + 1]
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:  # corner case
            return 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                pass
            else:
                return i
        return len(nums) - 1


'''
B. binary search - 把nums[mid]看成是target
    if mid in asceding part, the peak on its right
    if mid in desceding part, the peak on its left
    if left==right, peak is itself.
    Method:
        1. corner case
        2. left boundary, mid, right boudary as 0, (len(nums) - 1) //2, len(nums) - 1 
        3. do while loop, l < r ，在r = l时，发现该值
            if nums[mid] < nums[mid + 1], l = mid + 1
            if nums[mid] > nums[mid + 1], r = mid
        4. return l
    Time complexity: O(logN)
    Space: O(1)
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:  # return peak value's index
        if nums is None:
            return None

        l, r = 0, len(nums) - 1
        while l < r:  # 在l = r时，退出，找到这个点
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:
                l = mid + 1
            if nums[mid] > nums[mid + 1]:
                r = mid

        return l
'''
找峰值，mid比对的区间是 nums[mid + 1]，这种情况当l 越界等于 len(nums)就会报错，
所以可以选择用 while l + 1 < r的区间，最终对l和r进行比对。当然也可以写Edge处理。
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:
                l = mid
            else:
                r = mid
        if nums[l] > nums[r]:
            return l
        else:
            return r