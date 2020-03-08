#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 9:12
# @Author  : LI Dongdong
# @FileName: 261. Graph Valid Tree.py
''''''
'''
题目分析
1.要求：Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

    Example 1:
    
    Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
    Output: true
    Example 2:
    
    Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    Output: false
    Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
2.理解:判断无向图是否为树，即一个顶点的的两个祖先是否是同一个，若是则在同一个组里，三点一定成环
3.类型：并查集
4.确认输入输出及边界条件：
    input: n: int; pair: list; elem in list , no repeated, no order
    output: T/F
    corner case: n is None? F; n is 0 F; n is 1, T; len(edge) != n - 1, F
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. Union-find set
    Method:
        1. create the group tag list, tag every node with its index as group tag
        2. scan the i, j of pair
             if i in group tag == j in group tag, i, j already connected, have circel, return False
             else: change j's tag as i
        3. return True
    time O(N) space O(N)
易错点：
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False

        groupTag = [i for i in range(n)]
        for i, j in edges:
            root1 = self.find(i, groupTag)
            root2 = self.find(j, groupTag)
            if root1 == root2:
                return False
            else:
                groupTag[root2] = root1
        return True

    def find(self, index, groupTag):
        if groupTag[index] == index:
            return index
        else:
            return self.find(groupTag[index], groupTag)

'''
B.DFS + parent tag
    Method:
        1. create visit list to tag if visited
        2. create the graph
        3. scan every node
            do dfs (visited, graph, index, -1 as parent) on the node
                if node visited and its parent is not index 
'''
class Solution:
    def validTree(self, n: int, edges) -> bool:
        if not n:
            return True
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False

        visited = [0] * n
        graph = [[] for _ in range(n)]

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        for i in range(n):
            if visited[i] == 0:
                if self.dfs(i, visited, graph, -1) == False:
                    return False
        return True

    def dfs(self, i, visited, graph, parent):  # True no cycle
        visited[i] = 1
        for j in graph[i]:
            if visited[j] == 0:
                if self.dfs(j, visited, graph, i) == False:
                    return False
            else:
                if parent != j:  # 若该点访问过，若无环，则j必是i的parent；若有环，则j不是i的parent
                    return False
        return True