#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 12:12
# @Author  : LI Dongdong
# @FileName: 209. Minimum Size Subarray Sum.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: 
    s, int; no limit
    nums; lenggh range is from 0 to inf; value range is no limit; have repeated value; no order
output:
    int, the minimal length 
corner case:
    if nums is none, return 0

A. brute force - two for loop
    Method:
        1. scan elem X from 0 - index
            scan elem Y from X + 1 index
                calculate X - Y sum
                if sum >= s, calculate length, and renew the res
                    break
                else:
                    move on Y
        2. return res
    Time complexity: O(N^3)
    Space: O(1)

B optimized brute force using prefix
Time complexity: O(n^2)
Space O(n)

C. slide window - keep a window by l and r pointer, in this windows, the sum of them >= s
    Method:
        1. set l, r from 0
        2. r move right, until sum from l to r >= s, renew the length
            l move right if sum from l to r >= s, renew the length, until sum < s
        3. run 2 step again, until r out of the range of nums
    Time: O(n^2)
    space: O(1)
核心：
    先r右移动到sum of l and r >= s，记录length, 更新res
    再移动l，记录length，更新res，直到sum < s
    再运行步骤1
    总之：先探索右边界，再适当缩小左边界
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0

        l = r = 0
        n = len(nums)
        res = float('inf')

        while r < n:
            if sum(nums[l:r + 1]) < s:
                r += 1
            else:
                res = min(res, r - l + 1)
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res


'''
D. slide window - 优化版
Time complexity: O(N)
Space: O(1)
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0

        l = r = 0
        n = len(nums)
        res = float('inf')
        total = 0

        while r < n:
            total += nums[r]
            while total >= s:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1

        if res == float('inf'):
            return 0
        else:
            return res

'''
binarySearch有问题，回来再修改
'''
'''
D. binary tree method
    Method: 
        1. get prefix sum
        2. scan elem i from 0-index
            from 1 to end index
            use binary search to find a j that prefix[j] - prefix[i] = sum
                if find use the j - i as the length
                else use l - i as the length
            renew the res
        Time complexity: O(nlogn)
        Space: O(n)
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:  # corner case
            return 0

        prefix = [nums[0]]
        for elem in nums[1:]:
            prefix.append(elem + prefix[-1])

        def binarySearch(target, arr):  # return target index in arr
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        res = float('inf')
        n = len(prefix)
        for i in range(n):
            target = s - prefix[i]
            j = binarySearch(target, prefix[i + 1:])
            res = min(res, j + 2)

        return res if res != float('inf') else 0


X = Solution()
print(X.minSubArrayLen(4, [1,4,4]))