#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 16:14
# @Author  : LI Dongdong
# @FileName: 713. Subarray Product Less Than K.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: nums, list; length range is from 0 to 5000; elem of nums range is from 1 to 999
    k, range is 0 to 10^6
output: 
    int, the subarray number which product < k
corner case
    nums is None, return 0

A.Two Pointer Method
    Method:
        1. l, r = 0 index
        2. move r to right, and add  to res, until product nums[l:r + 1] > k
            move l to right, until product nums[l:r + 1] < k
            continue move r
        3. return res
    Time complexity: O(N), N is length of nums
    Space: O(1)

易错点：
    1. l <= r的判断
    2.r的两种情况下都得进一位

'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        for right in range(len(nums)):
            # 右边界右移
            product *= nums[right]
            # 如果乘积>=k，左边界右移
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            # 当前右边界下，满足条件的数组
            count += right - left + 1
        return count

'''
k = 100
[10, 5, 2, 6]
     l
             r
prod = 1 * 10 * 5 * 2 / 10 = 10 * 6 
res = 1 + 2 + 3

k = 0
  [1, 2, 3]
         l
         r
prod = 1 / 1 = 1 *  2 /2 
res
'''