#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 9:25
# @Author  : LI Dongdong
# @FileName: 378. Kth Smallest Element in a Sorted Matrix.py
''''''
'''
题目概述：求一个已行排序矩阵中的第k小的数
题目考点：max heap
解决方案：
方法及方法分析：
time complexity order: O(n^2 * log(k))
space complexity order: O(k)
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

'''
方法2：技巧性太强，不懂
不过显然不是题目要求的,通过观察可以发现每一行每一列都是增序排列，所以可以每次只加横行或者纵列。但如何避免重复呢？
可以维持一个数组记录已经访问过的点，要是为了节约空间的话，借鉴网上大神的想法，只有当处于第一列时才往下遍历，否则只横向遍历。
'''
from heapq import *

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        # ans = None
        while k:
            ans, i, j = heappop(q)
            if j == 0 and i + 1 < m:
                heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heappush(q, (matrix[i][j + 1], i, j + 1))
            k -= 1
        return ans
