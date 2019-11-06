# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 21:49
# @Author  : LI Dongdong
# @FileName: lc 473.py


class Solution:
    def generate(self,i,nums,target,bucket):
        if i==len(nums):
            return True
        for j in range(4):
            if bucket[j]+nums[i]>target:
                continue
            bucket[j]+=nums[i]
            if self.generate(i+1,nums,target,bucket):
                return True
            bucket[j]-=nums[i]
        return False


    def makesquare(self, nums):
        if len(nums)<4:
            return False
        if sum(nums) % 4 !=0:
            return False
        nums.sort(reverse=-1)
        bucket=[0,0,0,0]
        target=sum(nums)/4
        return self.generate(0,nums,sum(nums)/4,bucket)



x=Solution()
if x.makesquare([1,1,2,2,2]):
    print("1")
else:
    print('0')