#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 9:25
# @Author  : LI Dongdong
# @FileName: 378. Kth Smallest Element in a Sorted Matrix.py
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
input: matrix, size range is from 0 to inf; value range is no limit; have repeated value; row value is increasing
    k, int, value range is from 1 to n^2
output: int, the kth smallest value
corner case
    matrix is None, return None

A. heap - keep a k max- heap, the top one is the result
    Method: 
        1. initial a heap
        2. scan elem in matrix, push -elem into the heap, keep the size of heap as k
        3. return the invert of top elem of the heap
    Time complexity: O(n^2 * log(k))
    Space: O(k)
'''
from heapq import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or matrix == [[]]:  # corner case
            return None

        heap = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                else:
                    heappushpop(heap, -matrix[i][j])
        return -heappop(heap)


