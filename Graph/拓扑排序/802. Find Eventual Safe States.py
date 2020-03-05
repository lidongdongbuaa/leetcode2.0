#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 14:51
# @Author  : LI Dongdong
# @FileName: 802. Find Eventual Safe States.py
''''''
'''
题目分析
1.要求：In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

    Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.
    
    Which nodes are eventually safe?  Return them as an array in sorted order.
    
    The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.
    
    Example:
    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
    Here is a diagram of the above graph.
    
    Illustration of graph
    
    Note:
    
    graph will have length at most 10000.
    The number of edges in the graph will not exceed 32000.
    Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1]
    
2.理解:DAG中，找到所有出度为0的点
3.类型：
4.确认输入输出及边界条件：

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A.本方法错误
易错点：
'''
class Solution:
    def eventualSafeNodes(self, graph):  # return list of safety node
        if graph == []:  # corner case
            return []
        if graph == None:
            return None

        indegree = [0] *  len(graph)
        outdegree = graph[:]

        for elem in outdegree:  # fulfil indegree
            for v in elem:
                indegree[v] += 1

        from collections import deque

        queue = deque([ i for i, val in enumerate(indegree) if val == 0])

        while queue:
            i = queue.popleft()
            for elem in outdegree[i]:
                indegree[elem] -= 1
                if indegree[elem] == 0:
                    queue.append(elem)
        res = [index for index, value in enumerate(indegree) if value == 0]
        return res

x = Solution()
x.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])

'''
B. topological sort
    Method:
        1. count indegree list [[1,3]...] and outdegree list [int] by graph
        2. push outdegree = 0 node to queue
        3. traversal the queue
            left pop the node
            save it to res
                scan its indegree node
                    the indegree node's outdegree - 1 as i
                    if i == 0, push this node to queue
        4. return sort res
            
易错点：sorted(res)和res.sort()的区别
'''
class Solution:
    def eventualSafeNodes(self, graph):  # return list of safety node
        if graph == []:  # corner case
            return []
        if graph == None:
            return None

        indegree = [[] for _ in range(len(graph))]
        outdegree = [0] * len(graph)

        for i, v in enumerate(graph):
            outdegree[i] = len(v)
            for elem in v:
                indegree[elem].append(i)

        from collections import deque
        queue = deque([x for x, value in enumerate(outdegree) if value == 0])

        res = []
        while queue:
            ind = queue.popleft()
            res.append(ind)
            for elem in indegree[ind]:
                outdegree[elem] -= 1
                if outdegree[elem] == 0:
                    queue.append(elem)
        return sorted(res)


'''
B. DFS to scan every node's path, if no cycle, save it
    Method:
        1. create visit [-1], 0 is visiting, 1 is finished
        2. scan every node
            do dfs() on them
                if dfs != False, save it in result set
        3. return res : 
        3. dfs(graph, visit, index) recursion, return True - no cycle, False has cycle
            end: 
                visit[index] is 1, return True
                visit[index] is 0, having cycle, return False
            
            visit[index] = 0
            trigger:
                scan all node of graph[index]
                    do dfs on these nodes
                        if dfs() is False, return False
            visit[index] = 1
            return True
    time complexity: O(V + E), space O(V)
易错点：不用考虑节点重复访问的问题，因为如果重复dfs的end条件就已经判断了
'''
class Solution:
    def eventualSafeNodes(self, graph):  # return list of safety node
        if graph == []:  # corner case
            return []
        if graph is None:
            return None

        visit = [-1] * len(graph)

        res = []
        for index in range(len(graph)):
            if self.dfs(index, graph, visit):
                res.append(index)
        return sorted(res)

    def dfs(self, index, graph, visit):
        if visit[index] == 1:
            return True
        if visit[index] == 0:
            return False

        visit[index] = 0
        for elem in graph[index]:
            if not self.dfs(elem, graph, visit):
                return False
        visit[index] = 1
        return True

