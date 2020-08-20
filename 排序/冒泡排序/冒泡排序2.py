#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 22:15
# @Author  : LI Dongdong
# @FileName: 冒泡排序2.py
''''''
'''
题目概述：降序 冒泡排序
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''

def bubbleSortAscending(arr):
    n = len(arr)

    for x in range(n):
        for y in range(x, n):
            if arr[x] > arr[y]:  # arr[x] < arr[y]: descending
                tmp = arr[x]
                arr[x] = arr[y]
                arr[y] = tmp
    print(arr)

bubbleSortAscending([1,7,2,3,4,5])
