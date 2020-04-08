#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 19:07
# @Author  : LI Dongdong
# @FileName: 300. Longest Increasing Subsequence.py
''''''
'''
题目概述：求一个array的最长上升子序列，sequence
题目考点：回溯；一维dp
解决方案：dp[i]代表以nums[i]结尾的最长上升子序列，因为需要明确上升的限制，故定义为以i结尾的子序列
方法及方法分析：回溯；dp
time complexity order: 回溯 O(2^n) > dp O(n^2) 
space complexity order: 回溯 O(2^n) > dp O(n)
如何考
'''
'''
find the longest increasing subsequence lenght

input: array, list; length range? from 0 to inf; vlaue range? no limit; repeated? N; order? N
output: int
corner case:
    nums is None? return 0
    nums is only one? return 1

A. brute force - all subsequence and find the increasing one
    method:
        1. corner case
        2. use backtracking to find all subsequence
        4. filter the increasing sequence, renew the result
        3. traversal the element in result, renew the longest lenght
    Time complexity: O(2^n)
    Space: in worst case,O(2^n)
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0
        if len(nums) == 1:
            return 1

        def backtrack(start, path):  # save all sequence in res

            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(0, [])

        def risingSeq(arr):  # return increasing sequence
            ans = []
            for elem in arr:
                if rising(elem):
                    ans.append(elem)
            return ans

        def rising(arr):  # return T for arr is increasing
            if len(arr) == 0:
                return False
            if len(arr) == 1:
                return True

            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True

        res = risingSeq(res)
        ans = 0

        for elem in res:
            ans = max(ans, len(elem))

        return ans


'''
B. DP method - dp
1. 原问题
    子问题：不同长度的序列的最长子序列，相互独立，没有相互制约
1. 状态 序列长度n
2. dp函数定义：
    首先明确dp[i]的含义：以nums[i]为结尾的最长上升子序列
    其次，思考 怎么由dp[0,..i-1]推出dp[i]
        以dp[i]举例， dp[i] = max(dp[i], dp[j] + 1), j from 0 to i - 1
    然后遍历所有的i from 0 to n
3. 边界状态：dp[i] = 1
Time: O(N^2)
Space:O(N)
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


'''
报错
C. binary tree  - patient sort
    Method:
        1. corner case
        2. 
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        top = [0] * len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]

            l, r = 0, piles
            while l <= r:
                mid = l + (r - l) // 2
                if poker < top[mid]:
                    r = mid - 1
                elif poker == top[mid]:
                    l = mid + 1
                else:
                    l = mid + 1

            if l > piles - 1:
                piles += 1
            top[l] = poker
        return piles


