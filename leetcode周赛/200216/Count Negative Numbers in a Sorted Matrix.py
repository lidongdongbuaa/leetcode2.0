#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 11:34
# @Author  : LI Dongdong
# @FileName: Count Negative Numbers in a Sorted Matrix.py
''''''
'''
题目分析
1.要求：Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

    Return the number of negative numbers in grid.
    
    Example 1:
    
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.
    Example 2:
    
    Input: grid = [[3,2],[1,0]]
    Output: 0
    Example 3:
    
    Input: grid = [[1,-1],[-1,-1]]
    Output: 3
    Example 4:
    
    Input: grid = [[-1]]
    Output: 1
2.理解：calculate the numb of negative numbers
3.类型：arr
4.确认输入输出及边界条件：
    input: m == n? N repeat? Y order? Y non- increasing, value range? -100 - 100
    output: int
    corner case: None [] [[]] -> 0; only one? Y
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路： brute force - count negative 
方法：
    scan every element
        if <0, count + 1
time complex: O(N)
space complex: O(1)
易错点：
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if grid is None:  # corner case
            return 0
        if grid == [[]]:
            return 0

        count = 0
        for row in grid:  # scan every elem
            for elem in row:
                if elem < 0:
                    count += 1
        return count


'''
思路： optimized brute force
方法：
    scan every row
        if row[0] < 0, left other elems < 0, count number
        if row[i] < 0, left elem of this row< 0, count number
time complex: O(N)
space complex: O(1)
易错点：
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if grid is None:  # corner case
            return 0
        if grid == [[]]:
            return 0

        m = len(grid)  # row number
        n = len(grid[0])  # column number

        count = 0
        for i in range(m):
            if grid[i][0] < 0:  # row[0] < 0 case
                count += (m - i) * n
                return count
            for j in range(n):  # row[i] < 0 case
                if grid[i][j] < 0:
                    count += n - j
                    break
        return count

'''
test case
corner case: None, [] ->0  [[]] -> 0
grid = [[1,-1],[-1,-1]]
m = 2, n = 2
count = 0
i = 0
j = 0 1
count =0 1
i = 1
count = (2-1)*2 + 1 = 3 
return 3
'''
