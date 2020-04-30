#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 12:21
# @Author  : LI Dongdong
# @FileName: Count Number of Teams.py
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
from head to end, choose arr which is ascedning or descending with 3 elem, soldier are unique

input: arr,list; lenght range? from 1 to 200; value range? 1 to 10^5; repeated value? N; oder? N
output: int; 
corner case
    length of arr < 3, return 0
    no such arr, return 0

A. brute force - backtracking
    Method:
        1. corner case
        2. find all 3 elem combination by backtracking, save them in list
        3. traversal the list, find the number of ascending or descending ones
        4. return
    Time: O(n^3)
    Space: O(n^3)

'''
from copy import deepcopy


class Solution:
    def numTeams(self, rating) -> int:
        if len(rating) < 3:  # corner case
            return 0

        def backtrack(i, item, res):  # return all combination of 3 elem
            if len(rating) - 1 < i:
                return

            item.append(rating[i])
            if len(item) == 3:
                res.append(deepcopy(item))
            backtrack(i + 1, item, res)
            item.pop()
            backtrack(i + 1, item, res)

        res = []
        backtrack(0, [], res)

        ans = 0
        for elem in res:
            if elem[0] < elem[1] < elem[2]:
                ans += 1
            elif elem[0] > elem[1] > elem[2]:
                ans += 1
        return ans


'''
B optimzed res space
'''
from copy import deepcopy


class Solution:
    def numTeams(self, rating) -> int:
        if len(rating) < 3:  # corner case
            return 0

        def backtrack(i, item, res):  # return all combination of 3 elem
            if len(rating) - 1 < i:
                return

            item.append(rating[i])
            if len(item) == 3:
                if item[0] < item[1] < item[2] or item[0] > item[1] > item[2]:
                    res.append(1)
            backtrack(i + 1, item, res)
            item.pop()
            backtrack(i + 1, item, res)

        res = []
        backtrack(0, [], res)

        ans = sum(res)
        return ans

'''
C.brute force
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:  # corner case
            return 0

        res = 0
        length = len(rating)
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        res += 1
        return res
