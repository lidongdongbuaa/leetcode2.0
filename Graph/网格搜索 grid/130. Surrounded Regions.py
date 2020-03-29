#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 10:47
# @Author  : LI Dongdong
# @FileName: 130. Surrounded Regions.py
''''''
'''
题目概述：在矩阵中，O被X包围或半包围，把被包围的O全部改为X
题目考点：矩阵的DFS/BFS； 逆向思维，求全包围的不好办，那就先求半包围的，剩下的就是全包围的
解决方案：把半包围的O改为M，然后把剩下的O，即被全包围的O改为X，把M改为O
方法及方法分析：DFS， BFS
time complexity order: O(N)
space complexity order: O(N)
如何考
'''
'''
transfer o to x which is in the region and not connect to border

input: matrix, x and o; shape range? [0:]
output:None
corner case：
    matrix is None -> return 
    matrix is only one elem -> return

逆向思维，先找不符合条件的o，即在边界和邻居在边界上的o，都标记一下，然后，把标记过的还原为o，未标记的改为x
A.DFS - from the board o to tag its neighbors, then flip untag o
    Method:
        1. corner case
        2. traversal every node
            from board o to dfs its neighbors, and tag them as 'M'
        3. traversal every node, change M to o, change o to x
    Time: O(N), N is total numb of nodes
    Space: O(N)

易错点：
    1. 在dfs中标记visited（本题不需要visited）
    2. 本题不需要visited，因为我改变了原grid，导致grid在从边界O开始访问前有两种状态，X和O，只访问O；访问后，O变为M,都不用访问了，故不用visited矩阵标记
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:  # corner case
            return

        r, c = len(board), len(board[0])

        def dfs(i, j):  # visited i, j neighbors and change o to M
            if i < 0 or i > r - 1 or j < 0 or j > c - 1 or board[i][j] == 'X' or board[i][j] == 'M':
                return

            board[i][j] = 'M'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r - 1 or j == 0 or j == c - 1) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'M':
                    board[i][j] = 'O'

'''
B. BFS - from border O to visit its neighbor and tag it
    Method:
        1. corner case
        2. traversal all node
            use bfs visit the border O node and its neighbors, tag as 'M'
        3. traversal all node
            change O to X
            change M to O
    Time: O(N) N is number of nodes
    Space: O(N/2) = O(N), in average; in worst case O(N)
'''
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == [[]] or board == []:
            return

        r, c = len(board), len(board[0])

        from collections import deque
        queue = deque()
        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r - 1 or j == 0 or j == c - 1) and board[i][j] == 'O':
                    queue.append([i, j])
                    board[i][j] = 'M'

        while queue:
            i, j = queue.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x <= r - 1 and 0 <= y <= c - 1 and board[x][y] == 'O':
                    board[x][y] = 'M'
                    queue.append([x, y])

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'M':
                    board[i][j] = 'O'