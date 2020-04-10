#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 20:20
# @Author  : LI Dongdong
# @FileName: Max Chunks to Sort Array.py
''''''
'''
题目概述：给一个不重复的arr，需要把其排序，现在可以采用分段的方式进行sort，即每一段sort，再拼接再一起，最多可以分为几段
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

corner case:
    1. arr is None -> 此种情况不存在
    2. arr is only one -> 1

Method:
    numb = 1
    1. traversal the  i  from 0 to n -2
        if arr[i] < min(arr[i + 1:])
            numb += 1
        return numb

'''
class Array:
    def cut(self, arr):
        if len(arr) == 1:
            return 1

        numb = 1
        for i in range(len(arr) - 1):
            if arr[i] < min(arr[i + 1:]):
                numb += 1
        return numb

x = Array()
print(x.cut([2,1,6,4,3,7]))