# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 21:39
# @Author  : LI Dongdong
# @FileName: lc 174.py

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        if dungeon==[]:
            return 0

        dp=[]
        row=len(dungeon)
        column=len(dungeon[0])
        for i in range(row):
            dp.append([])
            for j in range(column):
                dp[i].append(0)

        dp[row-1][column-1]=max(1,1-dungeon[row-1][column-1])
        for i in range(column-2,-1,-1):
            dp[row-1][i]=max(1,dp[row-1][i+1]-dungeon[row-1][i])
        for i in range(row-2,-1,-1):
            dp[i][column-1]=max(1,dp[i+1][column-1]-dungeon[i][column-1])

        for i in range(row-2,-1,-1):
            for j in range(column-2,-1,-1):
                dp_min=min(dp[i+1][j],dp[i][j+1])
                dp[i][j]=max(1,dp_min-dungeon[i][j])
        return dp[0][0]

x = Solution()
print(x.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
