#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 11:13
# @Author  : LI Dongdong
# @FileName: 133. Clone 图.py
''''''
'''
题目概述：图的克隆
题目考点：图节点的遍历
解决方案：图节点的遍历 + 遍历一个，则新建一个保存到dic里 + 连接neighbors
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
corner case: node is None, return None

A.dict save
    Method:
        1. scan node and its neighbor
            if node not in dic, copy the node as newNode
                sava node and newNode as key and value
            else, get the newCopy from dic
易错点：把先复制val，再复制neighbors的元素            
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        from collections import deque
        queue = deque([node])
        dic = {}
        dic[node] = Node(node.val) # 先复制node的val
        while queue:
            root = queue.popleft()
            for elem in root.neighbors: # 再复制node的neighbors元素
                if elem not in dic:
                    queue.append(elem)
                    dic[elem] = Node(elem.val)  # 复制node的neighbors元素的第一步:复制neighbors元素的val
                dic[root].neighbors.append(dic[elem]) # 复制node的neighbors元素的第二步:复制neighbors元素的neighbors元素
        return dic[node]

'''
dfs
核心思想：节点的遍历
    helper用来扫描每个节点，一旦扫描到节点，就复制放入dic中,并处理其neighbors部分。
易错点：
    在self.visited[root]的neighbors上append,而不是在self.visited[root]上加
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        self.visited = {}

        def helper(root):  # scan every node
            if root in self.visited:
                return

            self.visited[root] = Node(root.val)
            for elem in root.neighbors:
                helper(elem)
                self.visited[root].neighbors.append(self.visited[elem])
            return

        helper(node)
        return self.visited[node]


'''
A.DFS method
Steps:
    1. if node in dic, return node[dic]
    2. create node copy, save it in dict
    3. do 1, 2 on the node's neighbors

    Time complexity: O(n)
    Space: O(n)
'''


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        dic = {}

        def dfs(node):  # return copy node
            if node in dic:
                return dic[node]

            dic[node] = Node(node.val)

            for neigh in node.neighbors:
                dic[node].neighbors.append(dfs(neigh))

            return dic[node]

        return dfs(node)
