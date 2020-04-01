#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 11:00
# @Author  : LI Dongdong
# @FileName: 200. Number of Islands.py
''''''
'''
题目分析
1.要求：Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.
    
    Example 1:
    
    Input:
    11110
    11010
    11000
    00000
    
    Output: 1
    Example 2:
    
    Input:
    11000
    11000
    00100
    00011
    
    Output: 3
2.理解：count the single parts in the grid
3.类型：grid search
4.确认输入输出及边界条件：
    input: matrix [[]], row size and columns size are same? maybe
    output: int
    corner case:
        1. matrix is None? Y
        2. matrix is [[1]] or [[0]]? Y
        
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. DFS of grid
    Method:
     scan every unvisited inland and its neighbors at one time, the time of scan is our result
     1. create a visited grid with same size as map
     2. traversal every node from left to right, from up to down to find the unvisited island: i, record the times
        do dfs() on the i island to visited its 4 directional valid island
            End: i node out of bounder or i is visited or i is water
            Process: set i as visited
            Trigger: 4 directional dfs()
    3. return the times as result
    time complexity: O(M*N) space: O(M*N) implicit stack use
易错点：
    不要忘记标记访问点 visited[i][j] = 1
    times 是在for循环中 访问unvisited island累加的
    标志的是'1'，而不是数字1
'''
class Graph:
    def countIsland(self, grid):  # return numb of island
        if not grid:  # corner case
            return 0
        if grid == [['1']]:
            return 1
        if grid == [['0']]:
            return 0

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]  # 0 is unvisited
        times = 0

        def dfs(i, j):  # from [i, j] to search its neighbors
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or visited[i][j] == 1 or grid[i][j] == '0':  # end condition
                return

            visited[i][j] = 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i, j)
                    times += 1
        return times

'''
test code
'''
x = Graph()
# print(x.countIsland([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

'''
B. BFS
    Method:
        scan every node, when finding the unvisited island, push it into queue and visit its unvisited neighbor. 
        result is the times of finding the unvisited island
        1. create the visited table as same size as grid
        2. traversal every node left to right, up to down to find unvisited node
            record the times
            use queue to add the unvisited node and traversal its neighbor
        3. return times
    time complexity O(M*N); space complexity O(min(M,N)) but visited is O(M*N)
易错点：space complexity O(min(M,N))
'''
class Graph:
    def countIsland(self, grid):  # return number of island
        if not grid:  # corner case
            return 0
        if grid == [['0']]:
            return 0
        if grid == [['1']]:
            return 1

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        times = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    from collections import deque
                    queue = deque([(i, j)])
                    visited[i][j] = 1
                    while queue:
                        print(len(queue))
                        r, c = queue.popleft()
                        visited[r][c] = 1
                        if r - 1 >= 0 and visited[r - 1][c] == 0 and grid[r - 1][c] == '1':
                            queue.append([r - 1, c])
                            visited[r - 1][c] = 1
                        if r + 1 <= len(grid) - 1 and visited[r + 1][c] == 0 and grid[r + 1][c] == '1':
                            queue.append([r + 1, c])
                            visited[r + 1][c] = 1
                        if c - 1 >= 0 and visited[r][c - 1] == 0 and grid[r][c - 1] == '1':
                            queue.append([r, c - 1])
                            visited[r][c - 1] = 1
                        if c + 1 <= len(grid[0]) - 1 and visited[r][c + 1] == 0 and grid[r][c + 1] == '1':
                            queue.append([r, c + 1])
                            visited[r][c + 1] = 1
                    times += 1
        return times

x = Graph()
x.countIsland([[1,1],[1,1],[1,1]])
'''
test code
'''