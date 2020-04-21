#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 10:39
# @Author  : LI Dongdong
# @FileName: 611. Valid Triangle Number.py
''''''
'''
题目概述：判断一列数组里的数字是否可以组成三角形
题目考点：two pointer；
解决方案：固定长边，找其他两条边
方法及方法分析：
time complexity order: O(n^2)
space complexity order: O(1)
如何考
'''
'''
input: nums, list; length range is from 0 to inf; value is not repeated; no order
output: int, the number of triangle
corner case
    length of nums < 3, return 0


A. brute force - find all possible combinations and check them
    Method:
        use three for loop to produce all possible combination
        check the combination can make up the triangle
    Time complexity: O(n^3)
    Space: O(1)


A.有些问题，需要修正
A. two pointer method - scan the value and check it is triangle
    Method:
        1. sort the nums
            2,2,3,4
        2. scan elememt i from first one to last N0.3 one -> 2
            use two pointer, j, k to scan i's right elements
                j = 2, k = 4
                check if i and two pointers' elem can make up the triangle, 
                    if i + j <= k, k -= 1 or j += 1  -> 不存在的情况下 导致变化条件的产生
                    if i + j > k, j += 1, count the times
        3. return the times
'''
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         if len(nums) < 3:  # corner case
#             return 0

#         nums.sort()
#         times = 0
#         n = len(nums)
#         for i in range(n - 2):
#             j, k = i + 1, n - 1
#             while j < k:
#                 twoSum = nums[i] + nums[j]
#                 if twoSum > nums[k]:
#                     j += 1
#                     times += 1
#                 else:
#                     k -= 1
#         return times

'''
B. two pointer method - scan the value and check it is triangle
    Method:
        1. sort the nums
            2,2,3,4
        2. scan elememt i from last one to 3rd one
            i = 4
            use two pointer, j, k to scan i's left elements
                j = 2, k = 3
                check if i and two pointers' elem can make up the triangle, 
                    if j + k > i, count + k - j; k -= 1 (or j += 1?)， 此时 (j,k), (j + 1, k),...(k -1, k)都满足条件
                    if j + k <= i, j += 1
        3. return the times
    Time：O(n^2)
    Space: O(1)
易错点：two pointer都在twoSum里面
    每次判断条件只移动一个pointer
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:  # corner case
            return 0

        nums.sort()
        times = 0
        n = len(nums)
        for i in range(n - 1, 1, -1):
            j, k = 0, i - 1
            while j < k:
                twoSum = nums[j] + nums[k]
                if twoSum > nums[i]:
                    times += k - j
                    k -= 1
                else:
                    j += 1
        return times