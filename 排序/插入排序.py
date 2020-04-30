#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 20:14
# @Author  : LI Dongdong
# @FileName: 插入排序.py
''''''
'''
题目概述：插入排序
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
class Sort:
    def insertSort(self, nums):  # return sorted nums
        if not nums or len(nums) == 1:
            return nums

        n = len(nums)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

X = Sort()
print(X.insertSort([9,8,7,6,5,4,4,3,2,1]))