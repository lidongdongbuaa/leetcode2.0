#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 19:51
# @Author  : LI Dongdong
# @FileName: 88. Merge Sorted Array.py
''''''
'''
题目概述：把已排序数组b合并到已排序数组a中，要求合并后的数组也是已经排序的
题目考点：two pointer；two point完毕之后剩余数组的处理
解决方案：分离双指针数组 + 剩余数组的处理
方法及方法分析：从头开始的分离双指针；从尾开始的分离双指针
time complexity order: O(m + n)
space complexity order: 从尾开始的分离双指针 O(1) < 从头开始的分离双指针 O(m)
如何考
'''
'''
input:
    nums1, nums2; length range is no limit; value range is no limit; have repeated value; ordered
output:
    None
corner case
    nums2 is None, return

A.merge sort
    Method:
        two pointer for begining
    
    Time: O(m + n)
    Space: O(m)
易错点：
    1. 最后复制剩下的部分的时候, 由于copy1(即原始num1）的后半部分是0，故尾追时，要及时截止，不要附加0到新nums1里了。nums1[k:] = copy1[i:m]
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return

        copy1 = nums1[:]
        i = j = k = 0
        while i < m and j < n:
            if copy1[i] <= nums2[j]:
                nums1[k] = copy1[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1

        if i < m:
            nums1[k:] = copy1[i:m]
        if j < n:
            nums1[k:] = nums2[j:n]
        return


'''
B. merge sort - from end to head
    Time: O(m + n)
    Space:O(1)
易错点：
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        if j >= 0:
            nums1[:k + 1] = nums2[:j + 1]