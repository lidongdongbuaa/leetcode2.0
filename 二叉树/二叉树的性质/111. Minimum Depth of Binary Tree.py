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
corner case: not root, return 0

核心思想： 求所有高度中的最小值
易错点：
    [1,2]的最小高度是2，不是1
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = float('inf')

        def helper(root, h):  # calculate the height of root to leaf in h
            if not root:
                return

            if not root.left and not root.right:  # 因为是判断点，故在前/中/后序时判断点都可以
                self.res = min(h, self.res)
            helper(root.left, h + 1)
            helper(root.right, h + 1)

        helper(root, 1)
        return self.res

'''
核心思路：分治
易错点：因为把[1,2]视为最短长度为2，故需要加上对单边树的判断条件
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l and r:
            return min(l, r) + 1
        else:  # 对单边树的判断条件
            return max(l, r) + 1

'''
bfs
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        queue = deque([(root, 1)])

        while queue:
            root, h = queue.popleft()
            if not root.left and not root.right:
                return h
            if root.left:
                queue.append([root.left, h + 1])
            if root.right:
                queue.append([root.right, h + 1])


