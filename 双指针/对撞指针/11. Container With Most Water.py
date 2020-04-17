#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 15:24
# @Author  : LI Dongdong
# @FileName: 11. Container With Most Water.py
''''''
'''
题目概述：求不同边长容器的最大盛水量
题目考点：two pointer的两边到中间的递进方法
解决方案： 不断移动短边到中间，更新盛水量
方法及方法分析：
time complexity order: O(n)
space complexity order: O(1)
如何考
'''
'''
input:
    nums, list; length range is from 2 to inf; have repeated value; no order
output:
    int, the max containing
corner case
    len(nums) == 2, return min(nums[0], nums[1])

A. brute force - find all possible containg, and renew the max one, return
    Time complexity: O(n^2)
    Space: O(1)

B. two pointer - move the shorter line, to renew the max one
    Method:
        1. set left i and right j pointer at the begining and end of the height
            e.g. i = 0, value = 1; j = 8, value = 7
        2. calculate the containg as res
            e.g.res = max(0, (8-0) * min(1, 7)) = 8
        3. move the shorter line inside, renew the max containing
            e.g move 1 to 2, i = 1, value = 8, res = max(8, (8-1) * min(8, 7)) = 49
        4. continue to move shortest line, until i = j
        5. return res
    Time complexity: O(n)
    Space O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:  # corner case
            return min(height)

        i, j = 0, len(height) - 1
        res = (j - i) * min(height[0], height[-1])

        while i < j:  # move shorter line
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            res = max(res, (j - i) * min(height[i], height[j]))

        return res
