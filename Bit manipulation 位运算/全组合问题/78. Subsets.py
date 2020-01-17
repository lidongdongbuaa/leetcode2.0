# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 16:57
# @Author  : LI Dongdong
# @FileName: 78. Subsets.py
''''''
'''
题目分析
1.要求：Given a set of distinct integers, nums, return all possible subsets (the power set).
    Note: The solution set must not contain duplicate subsets.
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
2.理解：数组中，所有可能性的组合
3.类型：bit，array
4.确认输入输出及边界条件：
    input: list, no repeat, no order
    output: list
    corner case: 
        input: []?Y, only one? Yes 
        output: [], [list]
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：brute force - backtracking
方法：
    1. try to add all elem of nums in subRes
    2. pop the last one, and add next one, until find all candidates
time complex: O(N*2**N)
space complex: O(2**N)
易错点：别漏了[[]]
'''
from copy import deepcopy
class Solution:
    def subsets(self, nums):
        if nums == []:  # corner case
            return [[]]
        if len(nums) == 1:
            return [ nums, [] ]

        length = len(nums)
        res = []
        tmp = []
        res.append([])
        res = self.generate(nums, 0, length, res, tmp)  # produce the all candidates
        return res

    def generate(self, arr, i, length, res, tmp):
        if i == length:
            return res

        tmp.append(arr[i])
        res.append(deepcopy(tmp))
        res = self.generate(arr, i + 1, length, res, tmp)
        tmp.pop()
        res = self.generate(arr, i + 1, length, res, tmp)
        return res

x = Solution()
print(x.subsets([1,2,3]))

'''
B.
思路：mask present in or not
方法：
    1. get length of nums, and total numb of all subset
    2. scan from total numb to 0 the in which in or not present as binary
        scan numb in binary, if 1, add nums[i]
time complex: O(N*2**N)
space complex: O(2**N)
易错点：
'''
class Solution:
    def subsets(self, nums):
        size = len(nums)
        n = 1 << size  # 位掩码个数, 即总结果的元素个数,
        res = []
        for i in range(n):  # 把每个数从0到n-1，每个数的binary代表一种分配方案，故分开逐个分析。分析其有几个1.
            temp = []
            for j in range(size): # 根据nums的长度限定分析size位的0/1
                if i >> j & 1:  # 根据当前位掩码是否为1决定是否加入数组该位
                    temp.append(nums[j])
            res.append(temp)
        return res




