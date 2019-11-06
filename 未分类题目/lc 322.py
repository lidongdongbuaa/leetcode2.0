# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 20:21
# @Author  : LI Dongdong
# @FileName: lc 322.py

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp=[-1]*(amount+1)
        # for i in coins:
        #     if  amount ==i:
        #         return 1
        #     dp[i]=1
        dp[0]=0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i-coins[j]>=0 and dp[i-coins[j]]!=-1:
                    if dp[i]==-1 or dp[i]>dp[i-coins[j]]+1:
                        dp[i]=dp[i-coins[j]]+1
        return dp[amount]

x=Solution()
print(x.coinChange([1,2,5],11))





