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
C. binary Search - search diagonals
    Method:
        1. corner case
        2. from top left to bottom right, scan every node,i
            a. scan i horizontal elements, if meet value, return true log(N),N = n,n-1, n-2,...1
            b. scan i vertical elements, do same things
        3. return False

    Time Complexity: O(logN + log(N-1) + ...) = O(logN!) < O(NlogN), N is min (rows, columns)
    space: O(1)

易错点：弄清l,r的前后顺序，在子函数中
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

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical = self.find(matrix, target, i, True)
            horizontal = self.find(matrix, target, i, False)
            if vertical or horizontal:
                return True
        return False

    def find(self, matrix, target, start, vertical):  # if find target, return True
        l = start
        if vertical:
            r = len(matrix) - 1
        else:
            r = len(matrix[0]) - 1

        while l <= r:
            if vertical:  # 纵向扫描
                mid = l + (r - l) // 2
                midV = matrix[mid][start]
                if midV == target:
                    return True
                if midV < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # 横向扫描
                mid = l + (r - l) // 2
                midV = matrix[start][mid]
                if midV == target:
                    return True
                if midV < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


'''
D.search space reduction
    Method:
        1. corner case
        2. initialize a pointer,i,  in bottom left of matrix
            if target > i, move it to right
            else: move i to up, until find the target
    Time complexity: O(n + m)
    space: O(1)

'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:
            return False

        r = len(matrix) - 1
        c = len(matrix[0]) - 1

        i = r
        j = 0

        while i >= 0 and j <= c:
            pointer = matrix[i][j]
            if pointer == target:
                return True
            if pointer < target:
                j += 1
            else:
                i -= 1

        return False