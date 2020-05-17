#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 17:14
# @Author  : LI Dongdong
# @FileName: 1452. People Whose List of Favorite Companies Is Not a Subset of Another List.py
''''''
'''
题目概述：
题目考点：求两个set之间的包含关系
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
利用set可以相减的性质
Method
Step:
    1. traverse i elem in c
        condition = False
        traverse j elem in c
            if i != j and not set(i) - set(j), condition  = False
        if not condition, res.append(i)
    return res
Time complexity: O(n^2)
Space: O(1)

'''


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        c = favoriteCompanies
        n = len(c)
        dic = {index: set(val) for index, val in enumerate(c)}

        res = []
        for i in range(n):
            condition = False
            for j in range(n):
                if i != j and not (dic[i] - dic[j]):
                    condition = True
            if condition == False:
                res.append(i)
        return res

