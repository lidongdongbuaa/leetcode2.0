#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 8:06
# @Author  : LI Dongdong
# @FileName: 1443. Minimum Time to Collect All Apples in a Tree.py
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
    n, int; value range is from 0 to inf
    edge, list[list]; lengh range is from 0 to inf
    has Apple; list, length == n
output:
    int, the times needed to get the apples
corner case:
    if n == 0 or not edge or not hasApple, return 0

Method: DFS - check the tree has apple, if has, res += 2
Steps:
    1. use self.res = 0, build graph
    2. do dfs to traverse the tree, if find the apple, return True
        if hasApple[i], iHas = True, else, False
        explore i's neighbor
            if i's neighbor has apple,  res += 2, nHas = true
            else, nHas = False
        return nhas or iHas
    3. return res
易错点：for循环里，只要有一个nHas为true，则输出nHas = True
'''


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not n or not edges or not hasApple:
            return 0

        if n == 1:
            return 0

        self.res = 0
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)

        def dfs(i):  # traverse the tree, if has apple, return True
            nHas = False
            for nxt in graph[i]:
                if dfs(nxt):
                    nHas = True
                    self.res += 2
            return hasApple[i] or nHas

        dfs(0)
        return self.res


