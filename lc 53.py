# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 16:09
# @Author  : LI Dongdong
# @FileName: lc 53.py

class Solution:
    def maxSubArray(self, nums) -> int:
        #使用列表作为数据结构储存dp各个状态的值
        dp=[0]*len(nums)
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            dp[0]=nums[0]
            return max(max(dp[0]+nums[1],nums[1]),nums[0])
        else:
            dp[0]=nums[0]
            for i in range(len(nums)):
                dp[i]=max(dp[i-1]+nums[i],nums[i])
            dp.sort()
            return dp[-1]

x=Solution()
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

