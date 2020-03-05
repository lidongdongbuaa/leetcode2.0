#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 16:55
# @Author  : LI Dongdong
# @FileName: 无向图的最长距离.py
''''''
'''
题目分析
1.要求：每个点有到最远点的距离，找出这些最远距离的最小值
2.理解：
3.类型：
4.确认输入输出及边界条件：
    input: N:int, numb of node, list[[x1,y1]...]:x connect to y;no repeated, order? No; N range? [2,50]; no cycle ; Xi , Yi> 1
    output: int
    corner case: No
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. bfs to find all level + find min 
    Method:
        1. create visited dict[1] and graph dict {index : []}
        2. traversal every node to do bfs(index, graph, visit) to get every node's longest path
            a. queue.append([index, level])  
            b. traversal queue
                index, level = queue.popleft
                visit[index] = 1
                for elem in graph[index]
                    if visit[elem ] == 0：
                        queue.append([elem, level + 1])
                add level to longest
            c.add longest to res
            d. return min(res)
    time O(V + E) spave O(V)     
易错点：
'''
from collections import defaultdict, deque


class Solution:
    def findPath(self, n, pairs):  # return int
        graph = defaultdict(list)

        visited = {i: 0 for i in range(1, n + 1)}

        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)

        res = []

        for i in range(1, n + 1):
            v = visited.copy()
            g = graph.copy()
            path = []
            self.bfs(i, v, g, path)
            longest = max(path)
            res.append(longest)
        return min(res)

    def bfs(self, i, v, g, path):  # return longest path int
        queue = deque([(i, 1)])
        while queue:
            ind, level = queue.popleft()
            v[ind] = 1
            for elem in g[ind]:
                if v[elem] == 0:
                    queue.append([elem, level + 1])
                else:
                    path.append(level)
        return

''
'''
优化版
不用求所有的path，输出最后的level即可
'''
from collections import defaultdict, deque
class Solution:
    def findPath(self, n, pairs):  # return int
        graph = defaultdict(list)

        visited = {i: 0 for i in range(1, n + 1)}

        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)

        res = []

        for i in range(1, n + 1):
            v = visited.copy()
            g = graph.copy()
            longest = self.bfs(i, v, g)
            res.append(longest)
        return min(res)

    def bfs(self, i, v, g):  # return longest path int
        queue = deque([(i, 1)])
        while queue:
            ind, level = queue.popleft()
            v[ind] = 1
            for elem in g[ind]:
                if v[elem] == 0:
                    queue.append([elem, level + 1])
        return level - 1


'''
B. DFS to find the path height
    Method:
        1. traversal all node
            a. find all path length of one node by dfs
                1. build graph and visited
                2. apply dfs(graph, visit, index, tmp, length) 
                    End: visit[index] == 1 return 
                    Process: visit[index] = 1, add length to tmp
                    Trigger: for elem in graph[index], dfs(graph, visit, index, tmp, length + 1)      
            b. find the longest of these path
            c. save the longest in res
        2. find the min of res
    time complexity O(V+ E), space O(V)
'''

from collections import defaultdict
def findPath(n, pair):  # return int
    visited = {x: 0 for x in range(1, len(n) + 1)}
    graph = defaultdict(list)

    for i, j in pair:
        graph[i] = graph[j]
        graph[j] = graph[i]

    res = []
    for ind in range(1, n + 1):
        tmp = []
        v = visited.copy()
        length = 0
        dfs(graph, v, ind, tmp, length)
        longest = max(tmp)
        res.append(longest)
    return min(res)

def dfs(graph, v, ind, tmp, length):  # save all path length in tmp
    if v[ind] == 1:
        return

    v[ind] = 1
    tmp.append(length)
    for elem in graph[ind]:
        dfs(graph, v, elem, tmp, length + 1)
    return

