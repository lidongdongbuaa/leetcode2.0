#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 20:01
# @Author  : LI Dongdong
# @FileName: 240. Search a 2D Matrix II.py
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
every node in every row is sorted

input: 
    matrix[[]]; None? Y -> False; [[]]? Y -> False ; repeated? N; order? Y
    target: int
output: True for have, else False


A. brute force - scan every node
    Method:
        1. corner case
        2. use two for loop to scan every node, if has, return True, else return False
    Time complexity: O(MN), M is row number, N is colunm number
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False


'''
B. binary search
    Method:
        1. corner case
        2. traversal every row
            use binary search to find the target in the row
    Time complexity: O(MlogN)
    Space: O(1)
易错点：无
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False

        def find(row):  # find target in row by binary search
            l, r = 0, len(row) - 1
            while l <= r:
                mid = l + (r - l) // 2
                midVal = row[mid]
                if target == midVal:
                    return True
                if target < midVal:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        for row in matrix:
            if find(row):
                return True
        return False