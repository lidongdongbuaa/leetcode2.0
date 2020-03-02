#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 20:13
# @Author  : LI Dongdong
# @FileName: 207. Course Schedule.py
''''''
'''
题目分析
1.要求：There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
    
    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
    
    Example 1:
    
    Input: 2, [[1,0]] 
    Output: true
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0. So it is possible.
    Example 2:
    
    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.
    Note:
    
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
2.理解：依赖关系
3.类型：graph 依赖关系
4.确认输入输出及边界条件：
    input: num:int, condition:[[]], num range? N, list in condition, the order of elem of list? 1, 2 means? first 2 then 1
    output:T/F
    corner case:  num = 0 -> True, condition = [] ->True 
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. Graph - DFS
    Method:
        build a adjacency table, show the rely connection of nodes
        traversal every nodes and its next node until end from first node
            if one node is visited for twice
                return False
        return True
    time complexity: O(V + E) space: O(V)
易错点：
'''


class Solution:
    def canFinish(self, nums, condition):  # return T/F
        if nums == 0:  # corner case
            return True
        if condition == []:
            return True

        graph = [[] for _ in range(nums)]
        visit = [-1 for _ in range(nums)]  # 三种状态，-1未访问，0正在DFS中访问，1已经访问

        for i, j in condition:  # build adjacency table
            graph[j].append(i)

        for i in range(nums):
            if visit[i] == -1:  # 只访问未访问的，相当于剪枝
                if not self.dfs(graph, visit, i):
                    return False
        return True


    def dfs(self, graph, visit, ind):  # when repeat, return True or False
        if visit[ind] == 0:
            return False
        if visit[ind] == 1:
            return True

        visit[ind] = 0
        for elem in graph[ind]:
            if not self.dfs(graph, visit, elem):
                return False
        visit[ind] = 1
        return True


x = Solution()
print(x.course(2, [[1, 0]]))

'''
B. topology method
    Method:
        1. build the indegree and outdegree list from the nums and condition
        2. scan indegree = 0 nodes one by one by queue
            scan the node's  connecting node - neigh, reduct the indegree of its neigh if it has
                it its indegree = 0, append it to the queue
        3. if indegree list != [0] * nums, return False, means having node cann't visit, it has cicle; else return True
    time O(V + E)  space(V）
'''

from collections import deque
class Solution:
    def course(self, nums, condition):  # return T/F
        if nums == 0:  # corner case
            return True
        if condition == []:
            return True

        indegree = [0 for _ in range(nums)]
        outdegree = [[] for _ in range(nums)]

        for i, j in condition:  # fulfil the degree list
            indegree[i] += 1
            outdegree[j].append(i)

        queue = deque()
        for i, value in enumerate(indegree):
            if value == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neigh in outdegree[node]:
                indegree[neigh] -= 1  # node的出度点的入度一定大于0
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if indegree == [0] * nums:
            return True
        else:
            return False
