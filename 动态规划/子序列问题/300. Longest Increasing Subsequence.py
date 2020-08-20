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
C. patient sort
    Method:
        1. corner case
        2. buidl several heap which top elem is increasing, traversal elem X in numbs
            if X < smallest numb of heaps' top, put X on the top of first heap top
            if X > biggest numb of heaps' top, build a new heap to hold X
            else: use binary search to find heap top the X belongs to
            2, 9, 10
            3, 5
            18, 7, 
            101 
        3. return the heap numbers
    Time: O(N) traversal every elem in numbs
    Space: O(N) in worst case, the heap used

'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        heap = [nums[0]]

        def binarySearch(heap, elem):  # return index of elem in heap, if not, return right value
            n = len(heap)
            l, r = 0, n - 1

            while l <= r:
                mid = l + (r - l) // 2
                if heap[mid] == elem:
                    return mid
                elif elem < heap[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        for elem in nums[1:]:
            if elem < heap[0]:
                heap[0] = elem
            elif heap[-1] < elem:
                heap.append(elem)
            else:  # elem in heap top value range
                index = binarySearch(heap, elem)
                heap[index] = elem
        return len(heap)


'''
input: arr, list; length range from 0 to inf; value range is no limit; have repeation
output: int, length 
corner: 
    arr is None, return 0
    arr size is 1, return 1

dp[i] the max length of LIS until i 
if dp[i] = max(dp[i - 1], 1 + x) -> x 要利用到前一个状态的i的取值，而dp要求只记录阶段的结果，即（状态的取值和由该状态直接可以index得的原数据arr的值），不能占用额外的空间，
比如到某一阶段时，记录此时的index的值，这样是不行的

故 换状态

dp[i] 以i结尾的最长序列的长度
if arr[i] > arr[i - 1]: dp[i] = dp[i- 1] + 1 1-> 错误，本方法求的是最长子串，substring
else:
    dp[i] = 1

base case: i == 0, dp[0] = 1 
res = max(dp)
'''
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # corner case
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return 1

#         # dp
#         n = len(nums)
#         dp = [0] * n

#         for i in range(n):
#             if i == 0:
#                 dp[0] = 1
#             elif nums[i] > nums[i - 1]:
#                 dp[i] = dp[i - 1] + 1
#             else:
#                 dp[i] = 1

#         return max(dp)
'''
test case
corner case: 
    nums is None, return 0
    len(nums) == 1, return 1
nums=[10,9,2,5,3,7,101,18]
                 i
n = 8
dp = [1,1,1,2,1,2,3,1]
i = 0, 
i = 1, nums[i- 1]> nums[i]
i = 2, >
i = 3, <
i = 4, >
i = 5, <
i = 6, < 
i = 7, >
'''
'''
修正方法
dp[i] - 以i结尾的最长序列的长度
if arr[i] > arr[j]: dp[i] = dp[j] + 1, j < i
else:
    dp[i] = 1
分类讨论：取不取0，1，2，..., i - 1
    nums[i]是否大于nums[0], 是：dp[0] + 1; 否：dp[i]
    nums[i]是否大于nums[1]
    nums[i]是否大于nums[2]
    ...
    nums[i]是否大于nums[i - 1]


'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # corner case
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        # dp
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            if i == 0:
                dp[i] = 1
                continue
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    pass

        return max(dp)