#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 8:39
# @Author  : LI Dongdong
# @FileName: 归并排序-递归法.py
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
input: list[int]
output: sorted list[int]
corner case: 
    nums is None, return None
    nums is only one, return nums
'''
class Sort:
    def mergeSort(self, nums):  # return sorted nums
        if not nums:
            return None
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        l = nums[:mid]
        r = nums[mid:]

        l = self.mergeSort(l)
        r = self.mergeSort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                nums[k] = l[i]
                k += 1
                i += 1
            else:
                nums[k] = r[j]
                k += 1
                j += 1

        if i < len(l):
            nums[k:] = l[i:]
        if j < len(r):
            nums[k:] = r[j:]

        return nums

X = Sort()
print(X.mergeSort([9,8,7,4, 5, 6, 3, 2, 1]))