#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 9:19
# @Author  : LI Dongdong
# @FileName: 80. Remove Duplicates from Sorted Array II.py
''''''
'''
题目概述：快慢指针
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: array, list; length range is from 0 to inf; value range, no limit; have repeated value; increasing order
output: int, length of new array
corner case
    if nums is None, return 0
    if len(nums) <= 2:return len(nums)

核心：
    1. 以s为基准，不断比较s和l的值
    2. 由于是把后面的数前移，故s每移动一次，都要用nums[f]对nums[s]重新赋值
    3. 本题f从1开始
A.slow - fast pointer
    Method:
        1. set s = 0, l = 1,count = 1, count 是f的计数, s是原位，即改变之后不挪后位
        2. if s val == l val
             count += 1
             if count = 2
                s += 1
                nums[s] = nums[f]
                f += 1
             elif count > 2:
                f += 1
            if s val != f val:
                s += 1
                nums[s] = nums[f]
                f + = 1
                count = 1
        3. return s + 1
 [1,1,2,2,3,3]            
          s           
              f
count = 2

'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:  # corner case
            return 0

        if len(nums) <= 2:
            return len(nums)

        s = 0
        f = 1  # 注意f从1开始
        n = len(nums)
        count = 1

        while f < n:
            if nums[s] == nums[f]:
                count += 1
                if count == 2:
                    s += 1
                    nums[s] = nums[f]
                    f += 1
                else:
                    f += 1
            else:   # 不相等替换模板
                s += 1
                nums[s] = nums[f]
                f += 1
                count = 1
        return s + 1







