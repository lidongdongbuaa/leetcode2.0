#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 20:10
# @Author  : LI Dongdong
# @FileName: Largest number X which occurs X times.py
''''''
'''
题目概述：给定一个arr，若有value等于出现次数的数，返回这样数的最大值，不存在的话，返回0
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

corner case:
    1. arr is None -> 0

Method:
    1. corner case
    2. transfer as dic, key is value, val is time
    3. ans = 0, traversal the dic, if key == val, ans = max(ans, key)
    4. return ans
'''
class Array:
    def find(self, arr):  # return int else 0
        if arr is None:
            return 0

        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        ans = 0
        for k, val in dic.items():
            if k == val:
                ans = max(ans, k)
        return ans

x = Array()
print(x.find([5,5,5,5,5]))
