#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 8:31
# @Author  : LI Dongdong
# @FileName: 求每层的节点.py
''''''
'''
题目概述：
题目考点：
优化核心：
易错点：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: root
output: list
corner case:
    not root, return []
    only one root, return [node.val]
'''

'''
BFS
in while loop, use for loop to scan all node in same level
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

'''
dfs  参数模式
root的高度为最小值，leaf为最大值
use parameters in dfs() to record level, use dict to record the level node number
'''
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
