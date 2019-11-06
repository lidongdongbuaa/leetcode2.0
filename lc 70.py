# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 11:32
# @Author  : LI Dongdong
# @FileName: lc 70.py

class Solution:
    def climbStairs(self,n):
        dp=[0]*(n+1)
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            dp[1]=1
            dp[2]=2
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

x=Solution()
print(x.climbStairs(1))