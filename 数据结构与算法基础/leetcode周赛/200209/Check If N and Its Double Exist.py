#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:35
# @Author  : LI Dongdong
# @FileName: Check If N and Its Double Exist.py
''''''
'''
题目分析
1.要求：Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
    More formally check if there exists two indices i and j such that 
2.理解：one elem is twice of another elem in arr
3.类型：array
4.确认输入输出及边界条件：
    input: 2<= len(arr) <= 50, -10^3 <= arr[i] <= 10^3, order?N, repeated? N
    output: bool
    corner case: None? N Only one? N 
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force
方法：
    1. double one elem
    2. compare it with other elems
    3. repeat it for all elems
time complex: O(N**2)
space complex: O(1)
易错点：
'''
class Solution:
    def checkIfExist(self, arr) -> bool:
        for i in range(len(arr)):
            left = arr[0:i] + arr[i + 1 : len(arr)]
            for elem in left:
                if arr[i] == 2 * elem or elem  == 2 * arr[i]:
                    return True
        return False



'''
思路：QuickSort
方法：
    1. choose first as pivot
    2. compare elem from right with the pivot, move smaller one to left. if pivot is twice or half of other elem, return
    3. compare elem from left with pivot, move bigger one to right. if pivot is twice or half, return True
    4. renew pivot 
    5. do move on left part and right part of arr
    6. return False
time complex: O(NlogN)
space complex: O(N)
易错点：
'''
class Solution:
    def checkIfExist(self, arr) -> bool:
        res = False
        arr, res = self.compare(arr, res)
        return res


    def compare(self, arr, res):
        if len(arr) == 0 or len(arr) == 1:  # corner case
            return arr, res

        i = l = 0
        j = r = len(arr) - 1
        pivot = arr[i]
        while i < j:
            while i < j and pivot < arr[j]:
                if pivot == 2 * arr[j] or  arr[j]  == 2 * pivot:
                    res = True
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot:
                if pivot == 2 * arr[i] or  arr[i]  == 2 * pivot:
                    res = True
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot
        arr[0:i], res = self.compare(arr[0:i], res)
        arr[i + 1: r + 1], res = self.compare(arr[i + 1:r + 1], res)
        return arr, res

x = Solution()
print(x.checkIfExist([-778,-481,842,495,44,1000,-572,977,240,-116,673,997,-958,-539,-964,-187,-701,-928,472,965,-672,-88,443,36,388,-127,115,704,-549,1000,998,291,633,423,57,-77,-543,72,328,-938,-192,382,179]))
