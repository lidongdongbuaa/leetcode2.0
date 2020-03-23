#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 19:23
# @Author  : LI Dongdong
# @FileName: 74. Search a 2D Matrix.py
''''''
'''
题目概述: 在一个二维矩阵里，判断target是否存在
题目考点：二维矩阵的二分搜索
解决方案：midVal = matrix[mid // c][mid % c]
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
find  a value in a 2D matix

input: 
    matrix, list[list]; len(matrix) is ? [0, +1000]; len(matrix row)? [0, +1000]; None?Y; elem in row is sorted? Y; the first integer of i row ? the last integer of i - 1 row? > ; 
    target, int; None? N; out of matrix range? Y
output: True: have the value; False

A. brute force - scan every value in matrix
    Method:
        1. corner case
        2. traversal matrix
            for i in row
                for j in columns
                    check matrix[i][j] == target, if true, return true
            return False
    Time complexity: O(N)
    Space complexity: O(1)
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or matrix == [[]]:  # corner case
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
        2. set left and right boundary, l, r as 0, row*column - 1
        3. do while loop, l <= r
            mid = l + (r - l) // 2
            midVal = matrix[mid // column][mid % column]
            if midVal == target, return T
            if midVal < target, move l as mid + 1
            else, move r as mid - 1
        return False

    time complexity: O(logMN)
    space: O(1)

易错点：
    求行：matrix // n
    corner case: matrix == []/[[]]
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or matrix == [[]]:  # corner case
            return False

        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            midVal = matrix[mid // n][mid % n]
            if target == midVal:
                return True
            if target < midVal:
                r = mid - 1
            else:
                l = mid + 1
        return False
