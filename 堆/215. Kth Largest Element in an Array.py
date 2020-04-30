#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 12:13
# @Author  : LI Dongdong
# @FileName: 215. Kth Largest Element in an 数组.py
''''''
'''
题目概述：返回list中第k大的数
题目考点：heap
解决方案：建立并维护一个含有k个值的heap，heap里的数是前k大数字，top是第k大数字
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: 
    nums, list; length range is from 0 to inf, value range is no limit; have repeated value; no order
    k, int, value range is from 1 to len(nums)
output:
    int, the Kth largest elem
corner case
    nums is None, return None

A. sort + index
    Method:
        1. sort the nums
        2. return nums[-k]
    Time complexity: O(nlogn) n is length of nums
    Space: O(1)

B.heap - keep a min heap of size k; the top elem is result
    Method:
        1. traversal the elem in nums O(N)
            append elem in a heap  O(logK)
            if size of heap > k, pop the top one
        2. return the pop of the heap

    Time complexity: O(NlogK)
    SpaceO: O(k) = O(1)
易错点：
    堆的操作复杂度由堆的大小决定
'''
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:  # corner case
            return None

        heap = []
        for elem in nums:
            heappush(heap, elem)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)


'''
一行代码版
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:  # corner case
            return None

        return nlargest(k, nums)[k - 1]