#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 11:00
# @Author  : LI Dongdong
# @FileName: 求点到点的所有路径.py
''''''
'''
题目概述：给定一个矩阵，求两点之间的所有路径
题目考点：求所有路径必须用dfs（回溯法），用visite的保证不往回走
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
没做出来
'''
'''
利用子集模板
先树状图像化，0是root，故path先加入[0]，visited[0][0] = 1
'''
class Solution:
    def findPath(self,  grid):
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for _ in range(m)]

        res = []
        def backtrack(i,j, path, visited):
            if [i, j] == [m -1, n - 1]:
                res.append(path[:])

            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                    visited[x][y] = 1
                    path.append(grid[x][y])
                    backtrack(x, y, path, visited)
                    path.pop()
                    visited[x][y] = 0

        visit[0][0] = 1
        backtrack(0, 0, [0], visit)
        return res


x = Solution()
print(x.findPath([[0, 1], [2,3]]))
