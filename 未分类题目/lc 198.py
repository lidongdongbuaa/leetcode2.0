# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 11:33
# @Author  : LI Dongdong
# @FileName: lc 198.py

class Solution:
    def rob(self, nums) -> int:
        dp = [0] *(len(nums)+1)
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0], nums[1])
        else:
            dp[1] = nums[0]
            dp[2] = max(nums[0], nums[1])
            for i in range(3,len(nums)+1):
                dp[i]=max(nums[i-1]+dp[i-2],dp[i-1])
        return dp[len(nums)]







x=Solution()
print(x.rob([1,2,3,1]))
