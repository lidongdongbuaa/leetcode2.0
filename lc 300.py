# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 14:15
# @Author  : LI Dongdong
# @FileName: lc 300.py

class Solution:
    # def lengthOfLIS(self, nums) -> int:
    #     if nums == []:
    #         return 0
    #     dp = [1] * len(nums)
    #     for i in range(len(nums)):
    #         for j in range(0, i):
    #             if nums[i] > nums[j]:
    #                 if dp[i] < dp[j] + 1:
    #                     dp[i] = dp[j] + 1
    #     dp.sort()
    #     return dp[-1]

    #########method3#################################
    # def binary(self,nums,target):
    #     index=-1
    #     begin=0
    #     end=len(nums)-1
    #     while index==-1:
    #         mid=(begin+end)//2
    #         if target==nums[mid]:
    #             index=mid
    #         elif target<nums[mid]:
    #             if mid==0 or target>nums[mid-1]:
    #                 index=mid
    #             end=mid-1
    #         elif target>nums[mid]:
    #             if mid==len(nums)-1 or target<nums[mid+1]:
    #                 index=mid+1
    #             begin=mid+1
    #     return index
    #
    #
    #
    # def lengthOfLIS(self, nums) -> int:
    #     if nums == []:
    #         return 0
    #     stack = []
    #     stack.append(nums[0])
    #     for i in range(len(nums)):
    #         if nums[i] > stack[-1]:
    #             stack.append(nums[i])
    #         elif nums[i] <= stack[-1]:
    #             pos=self.binary(stack,nums[i])
    #             stack[pos]=nums[i]
    #     return len(stack)


            #########method2#################################
    def lengthOfLIS(self, nums) -> int:
        if nums==[]:
            return 0
        stack=[]
        stack.append(nums[0])
        for i in range(len(nums)):
            if nums[i]>stack[-1]:
                stack.append(nums[i])
            elif nums[i]<=stack[-1]:
                # if len(stack)==1:
                #     stack[-1]=nums[i]
                # elif len(stack)>=2 and nums[i]>stack[-2]:
                #     stack[-1]=nums[i]
                for j in range(0,len(stack)):
                    if stack[j]>=nums[i]:
                        stack[j]=nums[i]
                        break
        return len(stack)

    #########method1#################################
    # def lengthOfLIS(self, nums) -> int:
    #     if nums == []:
    #         return 0
    #
    # dp = [0] * len(nums)
    # dp[0] = 1
    # for i in range(len(nums)):
    #     dp[i] = 1
    #     for j in range(0, i):
    #         if nums[i] > nums[j] and dp[i] < dp[j] + 1:
    #             dp[i] = dp[j] + 1
    # dp.sort()
    # return dp[-1]


x = Solution()
print(x.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
