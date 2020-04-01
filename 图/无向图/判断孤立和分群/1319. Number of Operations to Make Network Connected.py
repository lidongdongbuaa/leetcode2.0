#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 11:28
# @Author  : LI Dongdong
# @FileName: 1319. Number of Operations to Make Network Connected.py
''''''
'''
题目概述：求需要多少新的连接，才能把孤立部分的电脑连接完毕
题目考点：计算无向图孤立部分的个数
解决方案：dfs/Union-find set 查找孤立部分的个数
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
A. union find method
Time : O(m), m is length of connections
Space: O(n)

'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if not connections or connections == [[]]:
            return -1
        if len(connections) < n - 1:
            return -1

        def find(index):  # find group tag of index
            if index == groupTag[index]:
                return index
            else:
                return find(groupTag[index])

        times = 0
        groupTag = [i for i in range(n)]
        rank = [1] * n
        for i, j in connections:
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                times += 1
                if rank[root1] >= rank[root2]:
                    rank[root1] += rank[root2]
                    groupTag[root2] = root1
                else:
                    rank[root2] += rank[root1]
                    groupTag[root1] = root2

        res = n - times - 1
        return res

'''
B.DFS
    Method:
        1. corner case
        2. build the graph and visted list
        3. traversal every node i
            from i to visit its  neighbors by dfs
            count times
        4. return times - 1
    Time complexity: build graph O(Edge), dfs O(V)
    Space: O(V)
'''

from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if not connections or connections == [[]]:
            return -1
        if len(connections) < n - 1:
            return -1

        graph = defaultdict(set)
        visited = [0] * n

        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)

        def dfs(i):  # visited i and neighbors in depth
            visited[i] = 1
            for j in graph[i]:
                if visited[j] == 0:
                    dfs(j)
            return

        times = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                times += 1
        return times - 1
