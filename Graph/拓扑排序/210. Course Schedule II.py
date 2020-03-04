#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 10:26
# @Author  : LI Dongdong
# @FileName: 210. Course Schedule II.py
''''''
'''
题目分析
1.要求：There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
    
    Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
    
    There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
    
    Example 1:
    
    Input: 2, [[1,0]] 
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
                 course 0. So the correct course order is [0,1] .
    Example 2:
    
    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
                 courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
                 So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
    Note:
    
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
2.理解：
3.类型：
4.确认输入输出及边界条件：
    input:  int, and pairs [[a, b]] b must be finished before a, int range? N
    output: list of course index, if impossible, return []
    corner case:
        int is None? -> []
        int is only one? -> [only one]
        pairs is None? -> [i for i in range(nums)]

5.方法及方法分析：
time complexity order: O(V + E)
space complexity order: O(V)
6.如何考
'''
'''
topological sort method
Method:
    create indegree and outdegree list by int and pairs
    use a queue to scan node with 0 indegree
    add node index into res []
    scan this 0-in node’s outdegree nodes
    reduce their indegree with 1
    if indegree = 0, add them into queue
    if indegree == [0] * int, where all node visited, return res
    else return []
time complexity O(V + E)  space O(V) queue will contain all the vertices initially since all of them will have 0 in-degree
易错点： if prerequisites == []: return [x for x in range(numCourses)] 这个corner case 不要忘
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        if numCourses == 0:  # corner case
            return []
        if numCourses == 1:
            return [0]
        if prerequisites == []:
            return [x for x in range(numCourses)]

        indegree = [0] * numCourses
        outdegree = [[]] * numCourses #for _ in range(numCourses)]  # [[]] * numCourses?

        for i, val in prerequisites:
            indegree[i] += 1
            outdegree[val].append(i)

        from collections import deque
        queue = deque([i for i, v in enumerate(indegree) if v == 0])  # push indegree = 0 node into queue

        res = []
        while queue:
            i = queue.popleft()
            res.append(i)
            for neighbor in outdegree[i]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if indegree == [0] * numCourses:
            return res
        else:
            return []

x = Solution()
print(x.findOrder(3, [[1,0],[2,0]]))


'''
B DFS
3->4->1->2->0
先到最末端，然后从后往前依次加入stack, 1->2->0, stack 为[0,2,1]
遇到3，到最末端4， 后stack加入 [0,2,1,4,3]
再reverse stack输出
易错点：
        for elem in graph[ind]:
            if not self.dfs(graph, visit, elem, stack):
                return False
        需要每个elem都扫一遍，而不只是-1的才扫
        扫到0时，return False

'''
class Solution:
    def findOrder(self, nums, condition):  # return T/F
        if nums == 0:  # corner case
            return []
        if condition == []:
            return [i for i in range(nums)]
        if nums == 1:
            return [0]

        graph = [[] for _ in range(nums)]
        visit = [-1 for _ in range(nums)]  # 三种状态，-1未访问，0正在DFS中访问，1已经访问

        for i, j in condition:  # build adjacency table
            graph[j].append(i)

        stack = []
        for i in range(nums):
            if visit[i] == -1:  # 只访问未访问的，相当于剪枝
                if not self.dfs(graph, visit, i, stack):
                    return []
        return stack[::-1]


    def dfs(self, graph, visit, ind, stack):  # when repeat, return True or False
        if visit[ind] == 0:  # 代表ind正在本循环扫描
            return False
        if visit[ind] == 1:
            return True

        visit[ind] = 0
        for elem in graph[ind]:
            if not self.dfs(graph, visit, elem, stack):
                return False
        visit[ind] = 1
        stack.append(ind)
        return True

x = Solution()
x.findOrder(3, [[0,1],[1,2]])