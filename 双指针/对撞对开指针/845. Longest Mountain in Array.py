#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 10:38
# @Author  : LI Dongdong
# @FileName: 845. Longest Mountain in Array.py
''''''
'''
题目概述：求最长山脉长度
题目考点：对开指针
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: array, list; lenght range is from 0 to inf; value range is no limit; have repeat value; no order among the values
output: max length of mountain
corner case
    A length < 3, return 0

A. two pointer - 对开指针 
    Method:
        1. 先找到peak
        2.然后用左右两个对开指针，寻找最长左山脉和最长右山脉,计算最长的length，然后更新res
    Time: O(2n) = O(n)
    Space: O(1)
易错点：
    1. 注意i的取值范围，直接用A[l - 1]里的l- 1表示即可，即l - 1 >= 0, 不用化简
'''


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        n = len(A)
        res = 0
        for i in range(1, n - 1):
            if A[i - 1] < A[i] and A[i + 1] < A[i]:
                l = i
                r = i
                while l - 1 >= 0 and A[l - 1] < A[l]:
                    l -= 1
                while r + 1 < n and A[r] > A[r + 1]:
                    r += 1

                length = r - l + 1
                if res < length:
                    res = length
        return res


'''
[2,1,4,7,3,2,5]
       i
   l
           r
'''