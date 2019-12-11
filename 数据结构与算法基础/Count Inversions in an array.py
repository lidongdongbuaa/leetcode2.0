#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 12:12
# @Author  : LI Dongdong
# @FileName: Count Inversions in an array.py
''''''
'''
Count Inversions in an array
1.要求：nversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
    Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
    Example: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
2.理解：求全局的逆置对的数量
3.类型：array
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input: None? Y only one? Y repeat? N order? N range? N
    output: 0/0/...
    focus on time or space?
'''

'''
idea：Merge sort method
Method：
    divide A in to groups of at most one elements
    compares, sort, merge every two groups (i, j), if i > j, numb+1
    compare left two group of two elements, if i > j, i+1...>j, numb + length(left) - i (including i)
    Then repeat the above process, until only one group left
    return  numb
time complex: O(NlogN)
space complex: O(N)
易错点：inv_count = inv_count + (len(L) - i) <- (mid - (i+1) +1)
'''


class Solution:
    def countInversions(self, arr):  # count inversion number
        inv_count = 0
        if arr == []:
            return 0
        if len(arr) == 1:
            return 0

        length = len(arr)
        mid = length // 2
        L = arr[:mid]
        R = arr[mid:]

        inv_count = inv_count + self.countInversions(L)
        inv_count = inv_count + self.countInversions(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                inv_count = inv_count + (len(L) - i)  # (mid - (i+1) +1)
                k += 1
                j += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

        return inv_count

x = Solution()
print(x.countInversions([1, 20, 6, 4, 5]))
