#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 22:21
# @Author  : LI Dongdong
# @FileName: 1411. Number of Ways to Paint N × 3 Grid.py
''''''
'''
题目概述：染色问题，问红黄蓝的染色种类数
题目考点：数学组合问题，本层2色，有3种2色下层，2种3色下层；本层3色，有2种2色下层，2种3色下层
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''

class Solution:
    def numOfWays(self, n: int) -> int:
        if n == 1:
            return 12


        memo = {}
        def dp(i, color):  # return color combination numbers
            if (i, color) in memo:
                return memo[(i, color)]

            if i == 1 and color == 3:
                return 6
            if i == 1 and color == 2:
                return 6

            if color == 2:
                ans = dp(i - 1, 2) * 2 + dp(i - 1, 3) * 2
            elif color == 3:
                ans = dp(i - 1, 2) * 2 + dp(i - 1, 3) * 3
            memo[(i, color)] = ans
            return ans

        res = dp(n, 2) + dp(n ,3)  # 2 is two color, 3 is 3 color
        return res % (10**9 + 7)
