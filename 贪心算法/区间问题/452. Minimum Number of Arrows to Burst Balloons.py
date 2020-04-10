#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 20:28
# @Author  : LI Dongdong
# @FileName: 452. Minimum Number of Arrows to Burst Balloons.py
''''''
'''
题目概述：重叠区间射箭，问最少几箭，全部射完
题目考点：重叠区间，问最多几个不重叠的区间
解决方案：Greedy + sort
方法及方法分析：
time complexity order: O(nlogn)
space complexity order: O(1)
如何考
'''
'''
input: list[list]; length range is [0, 1000]; repeated? Y; ordered? N
output: int, the arrows number
corner case
    input is None, return 0

A. Greedy - count the max number of non-intersect intervals
    Method:
        1. corner case
        2. sort the points by elem's end value
            e.g. [1, 6], [2, 8], [7, 12], [10, 16]
        3. choose a elem  X with smallest end value, remove all elem which intersect with X
            X is [1, 6], because 6 is smallest end value
            remove [2, 8]
            X is [7, 12]
            remove [10, 16]

        4. repeat 3 step, until no elem left
        5. return X numbers
'''


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points or points == [[]]:  # corner case
            return 0

        points.sort(key=lambda x: x[1])

        X_end = points[0][1]
        count = 1

        for interval in points:
            start = interval[0]
            if X_end < start:
                count += 1
                X_end = interval[1]
        return count