# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 10:46
# @Author  : LI Dongdong
# @FileName: lc 120.py

class Solution:
    def minimumTotal(self, triangle) -> int:
        if triangle==[]:
            return 0

        dp=[]
        for i in range(len(triangle)):
            dp.append([])
            for j in range(len(triangle[i])):
                dp[i].append(0)

        for i in range(len(triangle[-1])):
            dp[len(triangle)-1][i]=triangle[-1][i]

        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(dp[i])):
                dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        return dp[0][0]



x = Solution()
print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
