# -*- coding: utf-8 -*-
# @Time    : 2/12/2020 11:25 AM
# @Author  : LI Dongdong
# @FileName: 104. Maximum Depth of Binary Tree.py
''''''
'''
题目概述：求一个树的最大高度
题目考点：dfs和bfs
解决方案：dfs，更新最大高度；bfs，累计最大高度
方法及方法分析：
time complexity order: O(n)
space complexity order: dfs:O(logN); bfs:O(N)
如何考
'''
'''
dfs 自下而上
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1

'''
dfs 自上而下
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        self.res = 0

        def dfs(root, h):
            if not root:
                return

            self.res = max(self.res, h)
            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
            return

        dfs(root, 1)
        return self.res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        self.res = 0

        def dfs(root, h):
            if not root:
                return

            self.res = max(self.res, h)
            h += 1
            dfs(root.left, h)
            dfs(root.right, h)
            h -= 1
            return

        dfs(root, 1)
        return self.res

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        stack = [(root, 1)]
        res = 0

        while stack:
            r, h = stack.pop()
            if r:
                res = max(res, h)
                stack.append([r.right, h + 1])
                stack.append([r.left, h + 1])
        return res

'''
bfs
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        from collections import deque
        queue = deque([(root, 1)])
        res = 0

        while queue:
            r, h = queue.popleft()
            if r:
                res = max(res, h)
                queue.append([r.left, h + 1])
                queue.append([r.right, h + 1])
        return res