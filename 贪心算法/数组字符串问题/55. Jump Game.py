#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 10:45
# @Author  : LI Dongdong
# @FileName: 55. Jump Game.py
''''''
'''
题目概述：给定一个list，元素是可以跳到步数，问是否可以跳到list的最末尾
题目考点：Greedy
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: list, length range is from 0 to inf; value range is from 0 to inf; have repeated, no order
output: True if can reach to end, else False
corner case:
    nums is None, return True
核心思想：
    在可选择的范围内，每次都选能够跳的最远的点
        1. 把nums(可以跳的步数)转化为farNums(从点开始，能够到达的最远点)
        2. 从第一个点开始扫描，在第一个点能够达到的范围内，选择具有最大值的点，即能够跳的最远点
'''
class Solution:
    def canJump(self, nums) -> bool:
        farIndex = [index + value for index, value in enumerate(nums)]

        i = 0
        pre = i
        maxRange = 0
        n = len(farIndex)
        while i < n:
            for j in range(pre, farIndex[i] + 1):
                if j < n - 1:
                    maxRange = max(maxRange, farIndex[j])
                else:
                    return True  # j reach to boarder or exceed the boarder
            if maxRange >= n - 1:
                return True
            if maxRange == i:
                return False
            pre = i
            i = maxRange
        return True

'''
B. Greedy
核心
    farIndex就是边界点的集合
    初始化范围为[0,farIndex[0]]，在此范围内，向右移动指针i，根据farIndex[i]的值，更新右边界，直到指针达到范围右边界或者nums的边界
Time complexity: O(n)
Space:O(n)
易错点：
    1. while中i的范围：什么时候跳出
        a. i可以到达end点，故是超出end点
        b. i可以到达右端点，故是超出右端点
    2. i的判断条件
        假设可以到达右端点，i = n 
'''
class Solution:
    def canJump(self, nums) -> bool:
        farIndex = [ind + val for ind, val in enumerate(nums)]

        end = farIndex[0]
        n = len(farIndex)
        i = 0
        while i <= end and i <= n - 1:
            if farIndex[i] > end:
                end = farIndex[i]
            else:
                i += 1
        if i == n:
            return True
        else:
            return False