#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 17:28
# @Author  : LI Dongdong
# @FileName: Largest M-aligned Subset.py
''''''
'''
题目概述：一个arr中，有一些数，在arr的index表示point numb, value表示值，给出M，求一个subset，让这些点的值两两都是M的倍数，问这个subset的长度
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

corner case
    1. arr is None:-> 0
    2. only one in arr -> 0
    2. M is 1 -> len(arr)

Method:
    1. sort the arr
    2. traversal i in the arr from 0 to n -2
        traversal j in arr from i to n - 1
             if j - i % m == 0
                tmp.append(j) 
        if len(tmp) > 0:
            tmp.append(i)
        ans = max(len(tmp), ans)
'''
class Array:
    def countLength(self, arr, M):
        if arr is None:
            return 0
        if len(arr) == 1:
            return 0
        if M == 1:
            return len(arr)

        arr.sort()

        ans = 0

        for i in range(len(arr) - 1):
            tmp = []
            for j in range(i + 1, len(arr)):
                if (arr[j] - arr[i]) % M == 0:
                    tmp.append(j)
            if len(tmp) > 0:
                tmp.append(i)
            ans = max(ans, len(tmp))
        return ans

x = Array()
print(x.countLength([-3,-2,1,0,8,7,1], 3))



