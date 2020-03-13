#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 9:02
# @Author  : LI Dongdong
# @FileName: 34. Find First and Last Position of Element in Sorted Array.py
''''''
'''
题目分析
求target的index range
    先确定target存在
    后转化为
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
B.binary search 
    Method:
        1. corner case
        2. use find1() to find the left position
            a. set left bonderay, l, as 0, set right boundary, r, as len(nums) - 1
            b. do while loop, l <= r
                find mid = l + (r - l) // 2
                if target = nums[mid], change r = mid - 1
                if target < nums[mid], cahnge r = mid - 1
                if target > nums[mid], change l = mid + 1
                return l as result
        3. use find2() to find the right position
            a. set left, and right bondary
            b. do while loop, l<= r
                find mid
                if target = nums[mid], change l = mid + 1
                ....if , if 
                return r as result
        4. return [l, r]
    Time complexity: O(logN)
    space: O(1)

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:  # corner case
            return [-1, -1]


        def findL():  # return target's first position
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif target < nums[mid]:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return l

        def findR():  # return target's last position
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if target == nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return r

        l = findL()
        r = findR()
        return [l, r]

'''
nums = [5,7,7,8,8,10], target = 8
1. pass corner case
2. get l
    l, r = 0, 5
    loop 1
        0 <= 5
        mid = 0 + 2 = 2
        nums[mid]= 7 < target 8
            l = 2 + 1 = 3
    loop 2
        3 <= 5
        mid = 4
        nums[mid] = 8 = target 8
            r = 3
    loop 3
        3 <= 3
        mid = 3
        nums[mid] = 8 = target
            r = 2
    loop 4
        3 <= 2
        return 3
    
3. get r
    l, r = 0, 5
    loop 1
        0 <= 5
        mid = 2
        nums[mid] = 7 < target 8
            l = 3
    loop 2
        3 <= 5
        mid = 4
        nums[mid] = 8 = target
        l = 4 + 1 = 5
    loop 3
        5 <= 5
        mid = 5
        nums[mid] = 10 > target
        r = mid - 1 = 4
    loop 4
        5 <= 4
        return 4
    4. return [l, r] -> [3, 4]
'''
