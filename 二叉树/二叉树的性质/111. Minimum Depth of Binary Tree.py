#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 13:55
# @Author  : LI Dongdong
# @FileName: 111. Minimum Depth of Binary Tree.py
''''''
'''
题目概述：求树的最小深度，以leaf为最底端
题目考点：分治 dfs ； bfs
解决方案：求所有的深度，返回最小的 dfs ； 直接求返回最小值；bfs返回第一个leaf的深度
方法及方法分析：
time complexity order: O(n)
space complexity order: dfs:O(logN); bfs:O(N)
如何考
'''
'''
input:root of tree; node number range is from 0 to inf; node value range is no limit; no order; have repeated
output: int, the shortest height
corner case:
    if not root, return 0
    
    
注意skewed tree时的返回值不是0
dfs 自下而上
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # corner case
        if not root:
            return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.left or not root.right:
            return max(l, r) + 1
        else:
            return min(l, r) + 1

'''
dfs 自上而下
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = float('inf')

        def dfs(root, h):  # scan every node
            if not root:
                return

            if not root.left and not root.right:
                self.res = min(self.res, h)
            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
            return

        dfs(root, 1)
        return self.res

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = float('inf')

        def dfs(root, h):  # scan every node
            if not root:
                return

            if not root.left and not root.right:
                self.res = min(self.res, h)
            h += 1
            dfs(root.left, h)
            dfs(root.right, h)
            h -= 1
            return

        dfs(root, 1)
        return self.res

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)]

        res = float('inf')
        while stack:
            root, h = stack.pop()
            if root:
                if not root.left and not root.right:
                    res = min(res, h)
                stack.append([root.right, h + 1])
                stack.append([root.left, h + 1])
        return res

'''
bfs
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # corner case
        if not root:
            return 0

        # build the queue
        from collections import deque
        queue = deque([[root, 1]])

        # use bfs to scan tree
        while queue:
            root, path = queue.popleft()
            if not root.left and not root.right:
                return path
            if root.left:
                queue.append([root.left, path + 1])
            if root.right:
                queue.append([root.right, path + 1])

        return 0

