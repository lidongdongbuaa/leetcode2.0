#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 20:21
# @Author  : LI Dongdong
# @FileName: 435. Non-overlapping Intervals.py
''''''
'''
题目概述：有重复区间，问删掉多少区间之后，区间不再重合
题目考点：区间sort；贪心寻找
解决方案：
方法及方法分析：
time complexity order: O(nlogn)
space complexity order: O(1)
如何考
'''
'''
input: list[list]; length range is from 0 to 1000; repeated? Y; order? N
output: int, the min numb of intervals to removed;
corner case:
    list is None, return 0

A. Greedy - sort and compare the first end with other start to delete
    Method:
        1. corner case
        2. based on the second value to sort the input in increasing order
            [1,2], [1,3], [2,3], [3,4]
        3. choose the first elem of list, compare its second value with other interval first value, 
            if first > the second value, count the number and renew index
            choose [1, 2]
                take 2, compare it with next 1 of [1,3], 2 > 1, so count = 1, index = 1
                take 2, compare it with next 2 of [2, 3], 2 == 2,so count = 1, index = 2
            choose interval[index = 2] = [2,3]
                take 3 compare it with next 3 o f[3, 4], 3 == 3, so count = 1, index = 3
            index = len(interval) - 1, return count
        4. repeat 3, until index out of list range
        5. return counted number

Time complexity: O(nlogn) for sorted
SpaceL O(1)
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or intervals == [[]]:  # corner case
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        n = len(intervals)
        i = 0
        count = 0

        while i < n - 1:
            end = sorted_intervals[i][1]
            while i + 1 <= n - 1 and end > sorted_intervals[i + 1][0]:
                count += 1
                i += 1
            i = i + 1
        return count


'''
test case
n = 4, i = count = 0
sorted = [1,2], [1,3], [2,3], [3,4]

i   = 0
end = 2, 3
    i + 1 = 1, 2, 3
    n - 1 = 3, 3, 3
    end =   2, 2, 3
    start = 1, 2, 3
        count = 1
        i     = 1
    i = 2, 3

'''


