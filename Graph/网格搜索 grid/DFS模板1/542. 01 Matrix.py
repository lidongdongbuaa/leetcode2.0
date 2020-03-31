#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 14:29
# @Author  : LI Dongdong
# @FileName: 542. 01 Matrix.py
''''''
'''
题目概述：在矩阵中，计算1到最近0点的最近距离，即从某点到外界的最短距离
题目考点：
    DFS, BFS; 
    逆向思维，计算a到b，可以通过计算b到a来完成；
    修改cell 1为极大值2**30 - 1，再通过比较进行缩小
    把起始点先全部放入queue中，后遍历；若cell被访问过，即不是极大值，那么其一定是最优值，原因是bfs一层一层遍历，被访问过，一定是上个0的更小层数访问得到的
解决方案：
    方案1：对每个1进行bfs，找到最近的0，tO(N^2)
    方案2：把1改为极大值，对每个0进行bfs，每进行一次bfs, 计算够到达的邻近1的距离，若邻近1不是初始极大值，则更新其值，其代表了到附近不同0的距离。tO(N)
方法及方法分析：方案1；方案2
time complexity order: 
space complexity order:O(N) 
如何考
'''
'''
find the distance from one No-0 to 0 distance

input: 
    matrix, list[[]]; shape range? None? only one elem? 
output:
    matrix
corner case
    matrix is None, return None
    matrix is [[]], return [[]]

A. brute force: BFS, record the distance from node to 0
    Method:
        1. corner case
        2. build a res matrix
        3. traversal the node in matrix 
            if node is not 0, bfs its neighbor and record the distance, if meet 0, return distance and add to res matrix

        Time complexity: O(N^2)
        Space: O(N)

易错点： 
    1. 超时！
    2. 空间复杂度巨大
'''
from copy import deepcopy


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:  # corner case
            return None
        if matrix == [[]]:
            return [[]]

        r, c = len(matrix), len(matrix[0])

        res = [[0 for _ in range(c)] for _ in range(r)]
        visit = [[0 for _ in range(c)] for _ in range(r)]

        def bfs(i, j, visited):  # visit i, j and its neighors, calculate the distance to 0 and add res
            from collections import deque

            queue = deque()
            queue.append([[i, j], 0])
            visited[i][j] = 1

            while queue:
                [i, j], d = queue.popleft()
                if 0 <= i - 1 and visited[i - 1][j] == 0:
                    if matrix[i - 1][j] == 1:
                        queue.append([[i - 1, j], d + 1])
                        visited[i - 1][j] = 1
                    else:
                        return d + 1
                if i + 1 <= r - 1 and visited[i + 1][j] == 0:
                    if matrix[i + 1][j] == 1:
                        queue.append([[i + 1, j], d + 1])
                        visited[i + 1][j] = 1
                    else:
                        return d + 1
                if j - 1 >= 0 and visited[i][j - 1] == 0:
                    if matrix[i][j - 1] == 1:
                        queue.append([[i, j - 1], d + 1])
                        visited[i][j - 1] = 1
                    else:
                        return d + 1
                if j + 1 <= c - 1 and visited[i][j + 1] == 0:
                    if matrix[i][j + 1] == 1:
                        queue.append([[i, j + 1], d + 1])
                        visited[i][j + 1] = 1
                    else:
                        return d + 1

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    pass
                else:

                    visited = deepcopy(visit)
                    d = bfs(i, j, visited)
                    res[i][j] = d
        return res


'''
超时
B. BFS - from 0 to search 逆向思维, 
    Method：
        1. corner case
        2. change 1 to max value in matrix
        3. traversal all 0 node, i,  by bfs, use queue to save note index and distance
            if i's neigbor is 0, return 
            else: 
                if distance < i's neighbor's value, replace it with distance and searhc its neighbors

        Time: O(N^2)
        Space: O(N)
'''


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix is None:
            return None
        if matrix == []:
            return []
        if matrix == [[]]:
            return [[]]

        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    matrix[i][j] = float('inf')

        def bfs(i, j):  # calculate distance from 0 to 1 and save in matrix
            from collections import deque

            queue = deque()
            queue.append([[i, j], 0])
            while queue:
                [i, j], d = queue.popleft()
                if 0 <= i - 1 and d + 1 < matrix[i - 1][j]:
                    queue.append([[i - 1, j], d + 1])
                    matrix[i - 1][j] = d + 1
                if i + 1 <= r - 1 and d + 1 < matrix[i + 1][j]:
                    queue.append([[i + 1, j], d + 1])
                    matrix[i + 1][j] = d + 1
                if 0 <= j - 1 and d + 1 < matrix[i][j - 1]:
                    queue.append([[i, j - 1], d + 1])
                    matrix[i][j - 1] = d + 1
                if j + 1 <= c - 1 and d + 1 < matrix[i][j + 1]:
                    queue.append([[i, j + 1], d + 1])
                    matrix[i][j + 1] = d + 1

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    bfs(i, j)
        return matrix


'''
C. BFS - from 0 to search 
    技巧：
        1. 把queue push node独立出来，减少计算时间，因为本来就需要全部遍历的
        2. 逆向思维,先把距离设置为最大值;距离通过到0的累计来计算
        3. 只访问未被访问的cell，一旦被访问，说明已经有最小值了，减少了时间复杂度
    Time: O(N), new cell are added to the queue only if their current distance is greater than the calculated distance, cells are not likely to be added mulitple times.
    Space: O(N)
'''
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix is None:
            return None
        if matrix == []:
            return []
        if matrix == [[]]:
            return [[]]

        r, c = len(matrix), len(matrix[0])

        res = [[0 for _ in range(c)] for _ in range(r)]

        from collections import deque
        queue = deque()

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    res[i][j] = 2**30 - 1
                else:
                    queue.append([i, j])

        while queue:
            i, j = queue.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x <= r - 1 and 0 <= y <= c - 1 and res[x][y] == 2**30 - 1:
                    queue.append([x, y])
                    res[x][y] = res[i][j] + 1


        return res



'''
超时， 要按照模板去写
D. DFS - find the 0 to its neighbor 1's shorest path length
    Method:
        1. corner case
        2. change 1 to inf
        3. traversal every 0 node, i
            dfs to search i's not 0 neighbors, if path < the neighbors' value, renew the value as path
        4. return matrix

    Time: O(N^2)
    Space: O(N) used by recursion stack
'''


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:  # corner case
            return None
        if matrix == [[]]:
            return [[]]

        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    matrix[i][j] = float('inf')

        def dfs(i, j, d):  # depth first search i,j's not 0 neighbor, and renew the path length
            if i < 0 or j < 0 or i > r - 1 or j > c - 1 or matrix[i][j] < d:
                return

            matrix[i][j] = d
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                dfs(x, y, d + 1)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    dfs(i, j, 0)
        return matrix
