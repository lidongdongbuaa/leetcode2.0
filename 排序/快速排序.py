#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 15:17
# @Author  : LI Dongdong
# @FileName: 快速排序.py
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
class Sort:
    def quickSort(self, nums):  # return sorted nums
        if not nums or len(nums) == 1:  # corner case
            return nums

        pivot = nums[0]
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[j] < pivot:
                nums[i] = nums[j]
                i += 1
            if nums[i] >= pivot:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        nums[:i] = self.quickSort(nums[:i])
        nums[i + 1:] = self.quickSort(nums[i + 1:])
        return nums

X = Sort()
print(X.quickSort([9,8,7,6,5,4,3,2,1]))
