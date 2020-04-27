#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 17:18
# @Author  : LI Dongdong
# @FileName: 376. Wiggle Subsequence.py
''''''
'''
题目概述： 给定一组数，具有上下波动特征，问最长的具有波动性的subsquence是多长
题目考点： 分析题意转化思想；贪心思想；前后比较方法
解决方案：最长的波动性序列就是极值点的个数，极值点构成最长波动性序列；用贪心思想找到极值点；先处理0-1，保存为pre，再处理后面的
方法及方法分析：
time complexity order: O(n)
space complexity order: O(1)
如何考
'''
'''
input: list, length range is from 0 to inf; value range is no limit, have repeated value; no order
output: the longest length of wiggle sequence
corner case:
    nums is None, return 0
    len(nums) is 1, return 1

A. dp, dp(i, state) is the longest wiggle when reach to nums[i]
    Method:
        if nums[i] > nums[i - 1]
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        if nums[i] == nums[i - 1]
        if nums[i] < nums[i - 1]
        等等。。先不看动态规划

B. greedy + two pointer 关键点在于找到转折点，即 (nums[i] - nums[i - 1]) * (nums[i + 1] - nums[i]) < 0 的点，故先进行0和1位的计算，保存为pre，再从2开始进行循环
    Method: 
        1. pre = nums[1] - nums[0]
        2. ans = 1 + (pre != 0)
        3. s = 1, f = 2
        4. while f < n
            if pre * (nums[f] - nums[s]) < 0, ans += 1, s = f, f+= 1
            else:
                f += 1
        5. return ans
     Time complexity O(N)
     Space: O(1)
[3,3,3,2,5]
       i 
pre = 3
count = 3
 
易错点：思考若前几个数相等时，怎么办
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0
        if len(nums) == 1:
            return 1

        pre = nums[1] - nums[0]
        count = 1 + (pre != 0)
        n = len(nums)
        i = 2

        while i < n:  # i是pre之前的点
            if pre * (nums[i] - nums[i - 1]) < 0 or (pre == 0 and nums[i] != nums[i - 1]):
                pre = nums[i] - nums[i- 1]
                count += 1
                i += 1
            else:
                i += 1
        return count






