#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 9:08
# @Author  : LI Dongdong
# @FileName: 归并排序-迭代法.py
''''''
'''
题目概述：归并排序-迭代法
题目考点：
解决方案：
方法及方法分析：
time complexity order: O(nlogn)
space complexity order: O(n)
如何考
'''
'''
input: list[int]
output: sorted list[int]
corner case: 
    nums is None, return None
    nums is only one, return nums
易错点：别忘记interval * 2
'''
'''
input: list[int]
output: sorted list[int]
corner case: 
    nums is None, return None
    nums is only one, return nums
易错点：
    1. 别忘记interval * 2
    2. 切片操作的本质是复制，故切片修改后，要赋值要原list上
'''
class Sort:
    def mergeSort(self, nums):  # return sorted nums
        if not nums:
            return None
        if len(nums) == 1:
            return nums

        interval = 1
        length = len(nums)

        def subSort(nums1, nums2):  # merge and sort two sorted list nums1 and nums2
            if not nums1:
                return nums2
            if not nums2:
                return nums1

            i = j = 0
            res = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

            if i < len(nums1):
                res += nums1[i:]
            if j < len(nums2):
                res +=nums2[j:]
            return res


        while interval < length:
            for i in range(0, length, 2 * interval):
                nums[i:i + 2 * interval] = subSort(nums[i:i + interval], nums[i + interval: i + 2 * interval])
            interval *=2
        return nums

X = Sort()
print(X.mergeSort([9,8,7,4, 5, 6, 3, 2, 1]))