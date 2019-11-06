# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 19:34
# @Author  : LI Dongdong
# @FileName: lc 64.py

class Solution:
    def minPathSum(self, grid) -> int:
        if grid==[]:
            return 0

        row=len(grid)
        column=len(grid[0])

        dp=[]
        for i in range(row):
            dp.append([])
            for j in range(column):
                dp[i].append(0)

        dp[0][0]=grid[0][0]
        for i in range(1,column):
            dp[0][i]=dp[0][i-1]+grid[0][i]

        for i in range(1,row):
            dp[i][0]=dp[i-1][0]+grid[i][0]

        for i in range(1,row):
            for j in range(1,column):
                dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]

        return dp[row-1][column-1]

x = Solution()
print(x.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
