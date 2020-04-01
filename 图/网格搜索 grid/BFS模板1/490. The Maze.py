#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 16:15
# @Author  : LI Dongdong
# @FileName: 490. The Maze.py
''''''
'''
题目概述：迷宫中的球是否可以碰到目标值
题目考点：迷宫算法
解决方案：BFS迷宫算法
方法及方法分析：BFS，DFS
time complexity order: 
space complexity order: 
如何考
'''
'''
check a ball could reach to a destination

input:
    maze, list; size range? more than 2;
    start, list;
    destination,list
output:
    T, F
corner case
    start == destination? N

A. bfs - detect ways
    Method:
        1. corner case
        2. use bfs to check the path
            a. build a queue and add start to it
            b. from the start, detect the longest and one direction the start can reach; from 4 directions
                check the path end, if it is the destination, return, else, append to the queue
    Time complexity: O(m * n), visited all cell only once
    Space: O(m *n) in worst case
'''


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        from collections import deque

        queue = deque([start])
        m, n = len(maze), len(maze[0])

        while queue:
            i, j = queue.popleft()

            maze[i][j] -= 1  # tag the cell visited

            if destination == [i, j]:
                return True

            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                row = x + i
                col = y + j

                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:  # move until the wall
                    row += x
                    col += y

                row -= x  # move back a step
                col -= y

                if maze[row][col] == 0 and [row, col] not in queue:
                    queue.append([row, col])
        return False

'''
B.DFS方法
需要进一步理解
'''
class Solution:
    def hasPath(self, maze, start, destination):
        m, n, stopped = len(maze), len(maze[0]), set()
        def dfs(x, y):
            if (x, y) in stopped:
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in (-1, 0) , (1, 0), (0, -1), (0, 1):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY):
                    return True
            return False
        return dfs(start[0], start[1])
