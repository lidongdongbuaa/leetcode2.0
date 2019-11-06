#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/12 20:59
#@Author: LI Dongdong
#@File  : lc 207.py
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree=[]
        graph=[]
        for i in range(numCourses):
            indegree.append(0)
            graph.append([])
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]=indegree[x]+1 #本有序对出现过几次，就加1
        print('graph is {}'.format(graph))

        Q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                Q.append(i) #在Q中添加indegree为0的，即入度为0的点的序号
        print('Q is {}'.format(Q))
        while len(Q)!=0:
            node_index=Q.popleft()
            for elem in graph[node_index]:
                indegree[elem]=indegree[elem]-1
                if indegree[elem]==0:
                    Q.append(elem)
        for i in range(numCourses):
            if indegree[i]!=0:
                return False
        return True




x=Solution()
x.canFinish(3,[[0,1],[0,2],[1,2]])