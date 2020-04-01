#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 9:00
# @Author  : LI Dongdong
# @FileName: 417. Pacific Atlantic Water Flow.py
''''''
'''
题目概述: 一个矩阵，值只能从高到低流动，问哪些值可以到达两个边缘
题目考点：逆向思维，把从点到边缘转化为边缘到中央；矩阵dfs
解决方案：从边逆流到中央的dfs
方法及方法分析：brute force - dfs every nodes; from margin to center dfs visit
time complexity order: brute force O(mn*mn) > from margin O(m*n)
space complexity order: O(m *n)
如何考
'''
'''
check whick node can reach to the boarder

input:  matrix; size range? from 0 to 150; value range, no limit
output: list[[position]] / no result, return []
corner case: 
    matrix is None or [[]], return []

A. brute force - let every node visit the grid, and then check it can reach to margin, and save to ans
    Method:
        1. corner case
        2. traversal every node 
            node dfs in the grid and record visited
            check the visited if reached to the margin
            if yes, add this node to res
        3. return res
    Time complexity: O(mn * mn)
    Space: O(m*n)
易错点：
    1. 思路简化 - 1.判断是否到达太平洋边沿-太复杂 -> 2.想到点直接访问，记录visit，然后判断visit
'''
class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or matrix == [[]]:
            return []

        m, n = len(matrix), len(matrix[0])

        def dfs(i, j, visited):  # let node to visit the gird
            visited[i][j] = 1
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0 and matrix[i][j] >= matrix[x][y]:
                    dfs(x, y, visited)
            return

        ans = []
        for i in range(m):
            for j in range(n):
                visited = [[0 for _ in range(n)] for _ in range(m)]
                dfs(i, j, visited)
                if (1 in visited[0] or 1 in [elem[0] for elem in visited]) and (1 in visited[m - 1] or 1 in [elem[-1] for elem in visited]):
                    ans.append([i, j])
        return ans


'''
B. DFs - from boarder to visite the water
    Method:
        1. corner case
        2. from Pacific ocean to dfs visite the water, tag in graph1
        3. from Atlantic ocean to dfs visite the water, tag in garph2
        4. find the common part of grahp1 and graph2
        5. return
    Time complexity: O(m*n) in worst case
    Space: O(H) H is height of the path, in worst case, it is m*n, recursion stack used
易错点：在最后比对a和p的visited时，两个节点都访问过，且都是1才是结果
'''


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or matrix == [[]]:  # corner case
            return []

        m, n = len(matrix), len(matrix[0])
        pVisited = [[0 for _ in range(n)] for _ in range(m)]
        aVisited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j, visited):  # from edge to visit water, tag visited cells
            visited[i][j] = 1
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0 and matrix[i][j] <= matrix[x][y]:
                    visited[x][y] = 1
                    dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, pVisited)
            dfs(i, n - 1, aVisited)
        for j in range(n):
            dfs(0, j, pVisited)
            dfs(m - 1, j, aVisited)

        ans = []
        for i in range(m):
            for j in range(n):
                if pVisited[i][j] == aVisited[i][j] == 1:
                    ans.append([i, j])
        return ans




