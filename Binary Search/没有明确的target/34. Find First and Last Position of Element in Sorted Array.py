#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 9:02
# @Author  : LI Dongdong
# @FileName: 34. Find First and Last Position of Element in Sorted Array.py
''''''
'''
题目分析
求target的index range
        l = 求 target前值（不明确）的r值，即比target前值大的最小值
        r = 求 target后值（不明确）的l值，即比target后值小的最大值

方法及方法分析：brute force - traversal; binary search
time complexity order: binary search O(logN) < brute force - traversal O(N)
space complexity order: binary search O(1) < brute force - traversal O(N)
6.如何考
'''
'''
find the index of first and last position of element  
O(logN) time 
binary search problem

input:nums[]; target,int; elements in nums may be repeated? Y; they have order? Y
output:int
corner case:
    nums is None? N
    targer is None? N
    target of out range of nums? Y ->[-1, -1]

A. brute force - traversal all element
    Method:
        1. corner case
        2. scan every  element  i in nums by for loop from 0 to len(nums) - 1
            if nums[i] == target, save is in res []
        3. if not res, return [-1,-1]
            else: return [res[0] and res[-1]]
    time complexity: O(N)
    space: O(N) - res use
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:  # corner case
            return [-1, -1]

        ans = []
        for index, val in enumerate(nums):
            if val == target:
                ans.append(index)
        return [ans[0], ans[-1]]

'''
B. binary search
    Method:
        1. corner case
        2.check T is out of range
        2. use binary search to find first position
        3. use binary search to find last position
    Time O(logN)
    Space O(1)
方法1： 提前处理T out of range + 判断nums[l] = T
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:  # corner case
            return [-1, -1]

        if target < nums[0] or target > nums[-1]:
            return [-1, -1]

        left = self.findFirst(nums, target)
        right = self.findLast(nums, target)

        return [left, right]

    def findFirst(self, nums, target):  # return the first index else return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid -1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        else:
            return -1

    def findLast(self, nums, target):  # return the last index else return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[r] == target:
            return r
        else:
            return -1


'''
求target的首末index，若无，返回-1

易错点：
    返回值的情况分类

    左端点值
        T大于nums：l = len(l)
        T在nums之内
            存在：nuns[l] = T
            不存在 nums[l] != T
        T小于nums nums[l] != T
方法二：对所有情况进行分类
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:  # corner case
            return [-1, -1]

        left = self.findFirst(nums, target)
        right = self.findLast(nums, target)

        return [left, right]

    def findFirst(self, nums, target):  # return the first index else return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l > len(nums) - 1:  # T大于all nums的情况,l为len(nums)
            return -1
        else:  # T在nums范围内，及小于all nums的情况
            if nums[l] == target:  # target在nums中存在的情况
                return l
            else:  # target在nums不存在，及target大于nums的情况
                return -1

    def findLast(self, nums, target):  # return the last index else return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if r < 0:  # T小于all nums的情况，r为-1
            return -1
        else:  # T在nums范围内，及大于all nums的情况
            if nums[r] == target:  # T在nums有
                return r
            else:  # T在nums里没有，及 T大于all nums的情况
                return -1

