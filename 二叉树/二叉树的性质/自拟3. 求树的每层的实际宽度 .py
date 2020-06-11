#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 8:31
# @Author  : LI Dongdong
# @FileName: 求每层的节点.py
''''''
'''
题目概述：求树的每层的实际宽度
题目考点：bfs / dfs自下而上
优化核心：
易错点：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''

'''
bfs
dfs自上而下
'''
class Tree:
    def findLevelNode(self, root):
        if not root:  # corner case
            return []

        if not root.left and not root.right:
            return [1]

        from collections import deque
        queue = deque([root])
        res = []

        while queue:
            n = len(queue)
            res.append(n)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

class Tree:
    def findLevelNode(self, root):
        if not root:  # corner case
            return []

        if not root.left and not root.right:
            return [1]

        from collections import defaultdict
        dic = defaultdict(int)

        def dfs(root, level):
            if not root:
                return

            dic[level] += 1
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            return

        dfs(root, 1)

        return [val for val in dic.values()]

class Tree:
    def findLevelNode(self, root):
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [1]

        dic = {}
        stack = [(root, 1)]

        while stack:
            root, level = stack.pop()
            if root:
                if level in dic:
                    dic[level] = 1
                else:
                    dic[level] += 1
                stack.append([root.right, level + 1])
                stack.append([root.left, level + 1])
        return [val for val in dic.values()]
