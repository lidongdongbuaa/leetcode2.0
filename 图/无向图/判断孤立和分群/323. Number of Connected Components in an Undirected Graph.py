#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 10:37
# @Author  : LI Dongdong
# @FileName: 323. Number of Connected Components in an Undirected 图.py
''''''
'''
题目分析
1.要求：Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
2.理解：找孤立的部分有几个,无向图的孤立点个数
3.类型：
4.确认输入输出及边界条件：
    input:n:int; edges: list[list]
    output：int
    corner case：
        1. n is None， return 0
        2 n is 1, return 1
        3. edge is [], return n

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. DFS to find numbs of do dfs 
    Method:
        1. build the visited list and the graph
        2. traversal every node and dfs() visit them and tag 1
            the times of dfs() is result
        3. return res
    time O(V + E) space O(V)
易错点：
'''
class Solution:
    def countComponents(self, n: int, edges) -> int:
        if not n:  # corner case
            return 0
        if n == 1:
            return 1
        if not edges:
            return n

        visited = [0] * n
        graph = [[] for _ in range(n)]

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        res = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, visited, graph)
                res += 1
        return res

    def dfs(self, i, visited, graph):
        if visited[i] == 1:
            return

        visited[i] = 1
        for elem in graph[i]:
            self.dfs(elem, visited, graph)
        return

'''
B. union-find method
    Method:
        1. tag every node's parent as index of the node in groupTag
        2. scan every pair [i, j] of edge
            find i's parent by dfs
            find j's parent by dfs
            if i's parent == j's parent, they are connected
            else: 
                change j's parent as i's parent
        3. count numb of changing, n - numb is result
    time O(N) space O(N)
易错点：
'''
class Solution:
    def countComponents(self, n: int, edges) -> int:
        if not n:  # corner case
            return 0
        if n == 1:
            return 1
        if not edges:
            return n

        groupTag = [i for i in range(n)]

        numb = 0
        for i, j in edges:
            root1 = self.find(i, groupTag)
            root2 = self.find(j, groupTag)
            if root1 == root2:
                pass
            else:
                numb += 1
                groupTag[root2] = root1

        return n - numb

    def find(self, i, group):
        if i == group[i]:
            return i
        else:
            return self.find(group[i], group)

x = Solution()
x.countComponents(4, [[0,3],[0,2],[1,2]])

