#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 22:31
# @Author  : LI Dongdong
# @FileName: 286. Walls and Gates.py
''''''
'''
题目概述：矩阵中有门和rooms，求每个rooms到门的最短距离 - 看到最短用bfs
题目考点：
    多次遍历整个矩阵时，先把起始点全部放到queue里；
    在全部放到queue的情况下，gate1扫第一层，gate2扫第一层，gate1扫第二层，gate2扫第二层...此时只要room的值发生改变，其值一定是最小的，故之后就不用再次扫描了
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
measure the distane from room to door, means get the path length

input: 
    matrix: [[]]; size range? 0 - inf
output:
    None
corner case:
    matrix is None or [] or [[]]? return None

A. bfs - from gate to search rooms and renew distance
    Method:
        1. corner case
        2. find all gate, push to queue, [i, j]
        3. traversal queue
            bfs to search its neighbor rooms and renew the distance to every rooms if the distance is smalller

    Time complexity: worst case O(N^2)
    space: O(N)
缺点：对gate共同联通的room重复计算path，故时间复杂度较高
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or rooms == [] or rooms == [[]]:  # corner case
            return None

        r, c = len(rooms), len(rooms[0])

        from collections import deque
        queue = deque()

        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue.append([i, j])

        while queue:
            i, j = queue.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x <= r - 1 and 0 <= y <= c - 1 and rooms[i][j] + 1 < rooms[x][y] and rooms[x][y] != -1 and \
                        rooms[x][y] != 0:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append([x, y])


'''
B. optimized bfs - from gate to search rooms and renew distance
    特点：room访问过一次之后，就不再访问了 -> 只访问未被访问过的rooms
    原因：bfs是层序遍历，加上本题先全部push gate, 故先访问gate1的第一层，再访问gate2的第一层，故一旦room被访问过，其一定是最短距离了
    故时间复杂度是 O(N)

    Time complexity: O(N)
    space: O(N)
易错点：
'''


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or rooms == [] or rooms == [[]]:  # corner case
            return None

        r, c = len(rooms), len(rooms[0])

        from collections import deque
        queue = deque()

        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue.append([i, j])

        while queue:
            i, j = queue.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x <= r - 1 and 0 <= y <= c - 1 and rooms[x][y] == 2 ** 31 - 1: # 只访问没有被访问过的rooms
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append([x, y])


'''
C. DFS - from gate to search rooms and fill the distance
    Method:
        1. corner case
        2. traversal 0 gate
            use dfs to search rooms and fill the rooms with the distance if current path < the value of the rooms
        Time: worst case O(N^N)
        Space: worset case O(N)
'''


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:  # corner case
            return None
        if rooms == [[]]:
            return None

        r, c = len(rooms), len(rooms[0])

        def dfs(i, j, d):  # from i, j to depth first search its neighbor
            if i < 0 or j < 0 or i > r - 1 or j > c - 1 or rooms[i][j] < d:
                return

            rooms[i][j] = d
            dfs(i - 1, j, d + 1)
            dfs(i + 1, j, d + 1)
            dfs(i, j - 1, d + 1)
            dfs(i, j + 1, d + 1)

        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)