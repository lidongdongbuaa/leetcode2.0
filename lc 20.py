# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 10:53
# @Author  : LI Dongdong
# @FileName: lc 20.py


from collections import deque


class Solution:
    def DFS(self, grid, mark, x, y):
        mark[x][y]='1'
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for m in range(len(dx)):
            newx=x+dx[m]
            newy=y+dy[m]
            if newx<0 or newx>=len(mark) or newy<0 or newy>=len(mark[newx]):
                continue
            elif mark[newx][newy]=='0' and grid[newx][newy]=='1':
                self.DFS(grid,mark,newx,newy)

    # def BFS(self, grid, mark, x, y):
    #     dx = [-1, 1, 0, 0]
    #     dy = [0, 0, -1, 1]
    #     q=deque()
    #     q.append([x, y])
    #     mark[x][y] = '1'
    #     while len(q)!=0:
    #         x = q[0][0]
    #         y = q[0][1]
    #         q.popleft()
    #         for i in range(len(dx)):
    #             newx = dx[i] + x
    #             newy = dy[i] + y
    #             if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[newx]):
    #                 continue
    #             elif mark[newx][newy] == '0' and grid[newx][newy] == '1':
    #                 q.append([newx,newy])
    #                 mark[newx][newy]='1'



    def numIslands(self, grid) -> int:
        island_num = 0
        mark = []
        for i in range(len(grid)):
            mark.append([])

            for j in range(len(grid[i])):
                mark[i].append('0')

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and mark[i][j] == '0':
                    # self.DFS(grid, mark, i, j)
                    self.DFS(grid,mark,i,j)
                    island_num += 1
                else:
                    continue
        print(island_num)


x = Solution()
x.numIslands(
    [["1", "1", "1", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
