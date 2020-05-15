#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 20:08
# @Author  : LI Dongdong
# @FileName: 1442. Count Triplets That Can Form Two Arrays of Equal XOR.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input:
    arr, list; length range is from 1 to 300; value range is from 1 to 10^8;have repeated value; no order
output:
    int, numbers of triplets
corner case
    len(arr) is 1, return 0

A.three for loop
Steps:
    1. scan i from 0 to n - 2
        scan j from i + 1 to n - 2
            scan k from j to n-2
                if a == b, res += 1
    return res
    time complexity: O(n^4)
    Space: O(1)

B. prefix XOR
    time: O(n^3)
'''


class Solution:
    def countTriplets(self, arr) -> int:
        if len(arr) == 1:
            return 0

        prefix = [arr[0]]
        for elem in arr[1:]:
            prefix.append(elem ^ prefix[-1])

        res = 0
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if i == 0:
                        a = prefix[j - 1]
                    else:
                        a = prefix[i - 1] ^ prefix[j - 1]
                    if j != k:
                        b = prefix[j - 1] ^ prefix[k]
                    else:
                        b = prefix[j - 1] ^ prefix[j]
                    if a == b:
                        res += 1
        return res


'''    
C. prefix XOR
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = b
a ^ b = 0 -> arr[i]^...^arr[k] = 0 -> 
    if i == 0: arr[i]^...^arr[k] = prefix[k]
    else: arr[i]^...^arr[k] = prefix[i - 1] ^ prefix[k] 

Time: O(n^2)
'''


class Solution:
    def countTriplets(self, arr) -> int:
        if len(arr) == 1:
            return 0

        n = len(arr)
        prefix = [arr[0]]
        for elem in arr[1:]:
            prefix.append(elem ^ prefix[-1])

        res = 0
        for i in range(n):
            for k in range(i + 1, n):
                if i == 0:
                    if prefix[k] == 0:
                        res += k
                else:
                    if prefix[i - 1] == prefix[k]:
                        res += k - i
        return res