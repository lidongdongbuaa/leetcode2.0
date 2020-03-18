#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 20:01
# @Author  : LI Dongdong
# @FileName: 240. Search a 2D Matrix II.py
''''''
'''
题目概述：一个矩阵，行内递增，列内递增，在此矩阵内判断一个值是否存在
题目考点：延矩阵对角线遍历，对对角线的点的行和列进行二分法求值； 搜索空间约简法
解决方案：如考点
方法及方法分析：1.search space reduction 2. diagonals binary search 3. row binary search 4. brute force - scan every one 
time complexity order: 1.search space reduction O(r + c) < 2. diagonals binary search O(nlogn), n is min(r,c) 3. row binary search O(clogr) 4. brute force - scan every one O(c*r)
space complexity order: O(1)
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
    Space: O(1)
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


'''
corner case:
    1. matrix is None/[[]] -> False
    2. target is None -> False

A. diagoal bianry search
    Method:
        1. corner case
        2. search from the left-up part of matrix to the right- bottom, i node
            binary search i node's horizontal and vertical element
    Time Complexity: O(logN!) < O(NlogN), N is min(m, n) m, n is row numbers, column numbers
    Space: O(1)
易错点：
    r的边界应该是 m/n - 1，这个减一不能忘
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:  # corner case
            return False
        if matrix == [[]]:
            return False
        if target is None:
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(min(m, n)):
            r = self.binarySearch(i, matrix, m, n, target, 1)
            c = self.binarySearch(i, matrix, m, n, target, 0)
            if r or c:
                return True
        return False

    def binarySearch(self, i, matrix, m, n, target, horizontal):  # return if the row or columns has target
        if horizontal == 1:
            r = n - 1
        else:
            r = m - 1
        l = i

        if horizontal == 1:
            while l <= r:
                mid = l + (r - l) // 2
                midVal = matrix[i][mid]
                if midVal == target:
                    return True
                if midVal < target:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            while l <= r:
                mid = l + (r - l) // 2
                midVal = matrix[mid][i]
                if midVal == target:
                    return True
                if midVal < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


'''
D.search space reduction
    Method:
        1. corner case
        2. from left bottom [len(matrix)][0] i,to search
            if i < target, move up
            if i == target return True
            if i > target, move right
    Time complexity: O(m + n)
    Space: O(1)
易错点：
    1.并不是每个格子都扫到，其实只扫了一行和一列，故tO(m + n)

'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:  # corner case
            return False
        if matrix == [[]]:
            return False
        if target is None:
            return False

        i = len(matrix) - 1
        j = 0

        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False