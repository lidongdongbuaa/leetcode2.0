#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 16:51
# @Author  : LI Dongdong
# @FileName: 求所有路径的深度.py
''''''
'''
题目分析
1.要求：求所有的路径深度
2.理解：
3.类型：dfs自上而下 / bfs
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
 input: tree root; root number range is from 0 to inf
 output: int
 corner case
    if root is None, return 0
    if only root, return 1
    
dfs自上而下；bfs
'''
class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        res = []
        def dfs(root, h):  # scan every node
            if not root:
                return

            if not root.left and not root.right:
                res.append(h)

            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
            return

        dfs(root, 1)
        return res


class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        stack = [(root, 1)]
        res = []

        while stack:
            root, h = stack.pop()
            if root:
                if not root.left and not root.right:
                    res.append(h)
                stack.append([root.right, h + 1])
                stack.append([root.left, h + 1])
        return res

class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        res = []
        from collections import deque
        queue = deque([(root, 1)])

        while queue:
            root, h = queue.popleft()
            if root:
                if not root.left and not root.right:
                    res.append(h)
                queue.append([root.left, h + 1])
                queue.append([root.right, h + 1])
        return res
