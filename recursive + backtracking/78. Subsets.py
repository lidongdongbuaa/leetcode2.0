# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 8:48
# @Author  : LI Dongdong
# @FileName: 78. Subsets.py

########################   ###########
import copy
class Solution:
    def generate(self, i, nums, item, result):
        if i == len(nums):
            return
        item.append(nums[i])
        result.append(copy.copy(item))
        self.generate(i + 1, nums, item, result)
        item.pop()
        self.generate(i + 1, nums, item, result)

    def subsets(self, nums) :
        item = []
        result = []
        self.generate(0, nums, item, result)
        return result

########################   ###########
import copy
class Solution:
    def __init__(self):
        self.result = []

    def generate(self, i, nums, item):
        if i == len(nums):
            return
        item.append(nums[i])
        self.result.append(copy.copy(item))
        self.generate(i + 1, nums, item)
        item.pop()
        self.generate(i + 1, nums, item)

    def subsets(self, nums) :
        item = []
        self.generate(0, nums, item)
        return self.result
########################   ###########
import copy
class Solution:
    def generate(self, i, nums, item, result):
        if i == len(nums):
            return
        item.append(nums[i])
        result.append(copy.copy(item))
        self.generate(i + 1, nums, item, result)
        item.pop()
        self.generate(i + 1, nums, item, result)

    def subsets(self, nums) :
        item = []
        result = []
        self.generate(0, nums, item, result)
        return result


x = Solution()
print(x.subsets([1,2,3]))
