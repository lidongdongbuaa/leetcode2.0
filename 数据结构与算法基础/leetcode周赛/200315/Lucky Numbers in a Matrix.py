#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 11:49
# @Author  : LI Dongdong
# @FileName: Lucky Numbers in a Matrix.py
''''''
'''
题目目的概述
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
find the value which is min in row and max in column

input:matrix[[int,int]]; len(matrix) range, [1,50]; len(matrix[0]) range,[1,50]; elem value range, [1, 10^5]; elem has order? N
output: the value, [int]
corner case: [[1]] -> 1; no lucky number? N 

A.brute force
    Method:
        1. corner case
        2. scan every row i
            scan row i's elem j
                if j is min of row i
                    compare j with same column value
                        if j is the max one
                            return j
        Time complexity: O(m * n)
        space: O(1)
易错点：题目要求返回的是[int],看清题目意思！！
'''


class Solution:
    def luckyNumbers(self, matrix):
        row = len(matrix)
        column = len(matrix[0])

        if row == 1 and column == 1:  # corner case
            return matrix[0][0]

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == min(matrix[i]):
                    if matrix[i][j] == max([x[j] for x in matrix]):
                        return [matrix[i][j]]
x = Solution()
print(x.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))