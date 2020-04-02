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
'''
'''
方案1：把初始节点当root，类比tree 求路径的普通方法
'''
class Solution:
    def findPath(grid):
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        def dfs(x, y, temp, visit, res):
            visit[x][y] = True

            temp.append(grid[x][y])
            if x == m - 1 and y == n - 1:
                res += [temp[:]]
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                    dfs(i, j, temp, visit, res)
            temp.pop()
            visit[x][y] = False

        res = []
        dfs(0, 0, [], visit, res)
        return res

    grid = [[0, 1, 2], [3, 4, 5]]
    print(findPath(grid))
    print(grid)

x = Solution()
print(x.findPath([[0,1,2],[3,4,5]]))

'''
方案2： 用回溯法，把初始设想为空，按照回溯的模板方法，把上下左右看作是选择列表
'''
def findPath2(grid):
    m, n = len(grid), len(grid[0])
    visit = [[False] * n for _ in range(m)]
    def dfs(x, y, temp, visit, res):
        visit[x][y] = True
        #print(temp)
        if x == m - 1 and y == n - 1:
            res += [temp[:]]
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                temp.append(grid[i][j])
                dfs(i, j, temp, visit, res)
                temp.pop()
        visit[x][y] = False
    res = []
    dfs(0, 0, [0], visit, res)
    return res
grid = [[0,1,2],[3,4,5]]
print(findPath2(grid))
#print(grid)
