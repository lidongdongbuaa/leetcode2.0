#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 13:01
# @Author  : LI Dongdong
# @FileName: 349. Intersection of Two Arrays.py
''''''
'''
题目概述：两个无序重复arr的交叉集
题目考点：set的去重，&和|的性质，set查询是O(1)的性质
解决方案：先set去重，再遍历一个与另一个进行in比较
方法及方法分析：two set, sorted binary search, brute force
time complexity order:  two set O(m + n)< sorted binary search O(nlogn + nlogm) < brute force Optimzed space O(m*n)
space complexity order: brute force Optimzed space O(1) < < sorted binary search O(m/n) < two set O(m + n)
如何考
'''
'''
find the intersection of two arrays

input: arr1, arr2 [int]; length range of arr1, arr2? [0, +10000];value range? [any]; elem of nums is repeated? Y; ordered? N
output: list[int]
corner case:
    one of arr is None: []
    both arr is None: []

A. Brute force
    Method:
        1. corner case
        2. use set to remove repeated values
        3. compare every elem,i of nums1 with nums2, if i in nums,append it to result
        4. return result
    Time complexity: O(m + n + m*n) = O(m * n), m is len(nums1), n is len(nums2)
    Space: O(m + n)

B. Optimzed space
    Method:
        1. corner case
        2. compare every elem i of nums1 with nums2, if in, add i in a set
        3. return the list(set)
    Time: O(m * n)
    Space: O(1)

C.sorted nums + two pointer 
    Method:
        1. corner case
        2. sorted nums
        3. pointe 1/2 to nums1/2, compare values and move pointers, if same, add to set
    Time：O(max(nlogn, mlogm))
    space: O(m + n)

d. sorted nums + binary search
    Method:
        1. corner case
        2. sorted one nums
        3. compare elem in unsorted nums with sorted nums, if in, add to set
    Time: O(nlogn + mlogn)
    space： O(n)

e. two set
    Method:
        1.corner case
        2. set two nums
        3. compare elems of nums1 with nums by in, if true, save it in res
        4.return res
    Time O(m + n + m * 1) = O(m + n)
    space O(m + n)

'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = set(nums1)
        arr2 = set(nums2)

        res = [x for x in arr1 if x in arr2]
        return res

