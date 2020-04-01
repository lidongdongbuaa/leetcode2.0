#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 22:07
# @Author  : LI Dongdong
# @FileName: 695. Max Area of Island.py
''''''
'''
题目概述：求岛屿面积
题目考点：矩阵的dfs的递归思想处理；已访问节点的记录方法：染色法和set记录法
解决方案：dfs染色法；dfs set记录法
方法及方法分析：
time complexity order: O(N)
space complexity order: O(N)
如何考
'''
'''
accumulate the area of island, find the biggest one

input: grid; size range? from 0 to 1000; value of it, 0/1
output: int; no island is 0
corner case
    grid is None or [[]], return 0

A. dfs - color the island and count the number
    Method:
    1. corner case
    2. scan every cell
        if cell is island and not color, dfs it, color the cell, and return the color times
        renew the times
    3. return the times

    Time compleixty: O(m*n), m is row, n is column, visit every node
    Space: O(m * n) in worst case， recursion stack use it
'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or grid == [[]]:  # corner case
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):  # return color times
            times = 1
            grid[i][j] = 2
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    times = times + dfs(x, y)
            return times

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans


'''
B. DFS
    use a seen to save the visited node
'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or grid == [[]]:  # corner case
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):  # return area
            seen.add((i, j))
            times = 1
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen and grid[x][y] == 1:
                    seen.add((x, y))
                    times += dfs(x, y)
            return times

        ans = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    ans = max(ans, dfs(i, j))
        return ans