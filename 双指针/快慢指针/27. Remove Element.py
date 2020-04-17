#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:23
# @Author  : LI Dongdong
# @FileName: 27. Remove Element.py
''''''
'''
题目概述：原位删除与目标值相同的数字
题目考点：快慢指针 - 有进阶做法
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: 
    nums, list; length range is from 0 to inf; have repeated value; no order
    val, int, value range, may out of range of nums
output:
    int, removed length of nums
corner case
    nums is None, return 0
    value is out of range of nums; return len(nums)

A. slow-fast pointer
    Method:
        1. set slow(s) and fast(f) pointer at 0,0
        2. while f < len(nums)
            if f= target, move f to right
            else:
                s value = f value
                s += 1
        3. return s + 1
    Time complexity: O(n), n is lenght of nums
    Space: O(1)
易错点：注意在while循环弹出时，输出值s在的位置
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:  # corner case
            return 0
        if val not in nums:
            return len(nums)

        s = f = 0
        n = len(nums)
        while f < n:
            if nums[f] == val:
                f += 1
            else:
                nums[s] = nums[f]
                s += 1
                f += 1
        return s


'''
val = 2
 [0,1,3,0,4,0,4,2]
            s

[3,2,2,3]
'''