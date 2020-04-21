#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 10:22
# @Author  : LI Dongdong
# @FileName: 1. Two Sum.py
''''''
'''
题目概述：给定sum，求nums中哪两个数的和为sum，输出这两个数的index
题目考点：
    1. use the same element twice，不能使用同一个值超过一次，并不意味着不能使用相同的值
    2. 新型比较方法：遍历nums，比较elem和它之前遍历过的数
        旧比较方法：遍历nums，比较elem和它之后的数
    3. 针对新型遍历方法，把遍历过的数加入dict，这样比较的时候，从O(n) 降维O（1）
解决方案：
    先遍历，用dic存贮已经遍历过的数
    判断要求的值是否在dic里
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
use the same element twice，不能使用同一个值超过一次，并不意味着不能使用相同的值
    e.g. 有两个2，则可以使用 2，2；但是如果只有一个2，则不能使用两次2
本题有重复的值
input: 
    nums, list; length range is from 1 to inf; no repeat; no order;
    target, int
output:
    indices, list


A. use dict save indices
    Method:
        1. scan every elem in nums
            calculate gap = target - elem
            if gap in dict,return elem index and gap's value
            else:
                save {elem :elem index} in dict

    Time complexity: O(N), N is length of nums
    Space: O(N)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in dic:
                return [i, dic[gap]]
            else:
                dic[nums[i]] = i

