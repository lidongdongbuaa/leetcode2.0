#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 7:24
# @Author  : LI Dongdong
# @FileName: 624. Maximum Distance in Arrays.py
''''''
'''
题目概述：求list[sub_list]，求sub_list里面的最大差值，差值不能出现在同一个sub_list里。
题目考点：linear scan; 双指针-数组;求差值，就是目前的极值与历史极值的差值，故scan sub_list更新结果和历史极值，
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: list[list]; length range is 2 to 10000; elements value range is from -1000 to 1000
output: int

A. single scan
    Method:
        1. 结果一定是历史最大/最小值与目前最小/最大值的差，故更新历史最大最下值，并更新差

Time complexity: O(N)
Space: O(1)
'''


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]

        res = float('-inf')

        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][-1] - minVal), abs(maxVal - arrays[i][0]))
            minVal = min(arrays[i][0], minVal)
            maxVal = max(arrays[i][-1], maxVal)

        return res



