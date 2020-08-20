#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 22:51
# @Author  : LI Dongdong
# @FileName: 冒泡排序.py
''''''
'''
题目概述：冒泡排序
题目考点：
解决方案：把大的元素往后调
方法及方法分析：
time complexity order: O(n^2)
space complexity order: O(1)
如何考
'''
class Sort:
    def bubbleSort(self, nums):  # return sorted nums
        if not nums or len(nums) == 1:
            return nums

        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

X = Sort()
print(X.bubbleSort([9,8,7,6,5,4,3,2,1]))