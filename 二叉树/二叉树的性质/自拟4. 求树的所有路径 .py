#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 8:30
# @Author  : LI Dongdong
# @FileName: 求所有路径.py
''''''
'''
题目概述：求树的所有路径，保存到list中
题目考点：
优化核心：
易错点：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

dfs自上而下
bfs
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def findAllPath(self, root):  # return [[path1], [path2]
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        res = []
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path[:])
                return

            if root.left:
                dfs(root.left, path + [root.left.val])
            if root.right:
                dfs(root.right, path + [root.right.val])
            return

        dfs(root, [root.val])
        return res

class Tree:
    def findAllPath(self, root):  # return [[path1], [path2]
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        res = []
        def dfs(root, path):
            if not root:
                return

            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
            return


        dfs(root, [])
        return res

class Tree:
    def findAllPath(self, root):  # return [[path1], [path2]
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        res = []
        stack = [(root, [root.val])]
        while stack:
            root, path = stack.pop()
            if root:
                if not root.left and not root.right:
                    res.append(path[:])
                if root.right:
                    stack.append([root.right, path + [root.right.val]])
                if root.left:
                    stack.append([root.left, path + [root.left.val]])
        return res

'''
bfs
'''
class Tree:
    def findAllPath(self, root):  # return [[path1], [path2]
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        res = []
        from collections import deque
        queue = deque([(root, [root.val])])

        while queue:
            root, path = queue.popleft()
            if not root.left and not root.right:
                res.append(path[:])
            if root.left:
                queue.append([root.left, path + [root.left.val]])
            if root.right:
                queue.append([root.right, path + [root.right.val]])
        return res

