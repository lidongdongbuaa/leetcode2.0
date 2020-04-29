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
corner case: root is None, return 0
核心思路：分治；每个node代表的高度是多少
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)

'''
bfs
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        queue = deque([(root, 1)])

        res = 0
        while queue:
            node, h = queue.popleft()
            if not node.left and not node.right:
                res = max(h, res)
            if node.left:
                queue.append([node.left, h + 1])
            if node.right:
                queue.append([node.right, h + 1])
        return res