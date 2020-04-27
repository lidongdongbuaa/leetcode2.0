#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:20
# @Author  : LI Dongdong
# @FileName: 101. Symmetric Tree.py
''''''
'''
题目概述：给定两个tree root，判定这两个tree是否相同
题目考点：多个tree的同时遍历
解决方案：dfs；bfs
方法及方法分析：
time complexity order: O(n)
space complexity order: dfs:O(logN); bfs:O(N)
如何考
'''
'''
corner case: root is None, return True

核心思路：分治；判定root的左右是否相等
'''
'''
dfs
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(l, r):  # judge the left and right is same
            if not l and not r:
                return True
            if not l or not r:
                return False

            if l.val == r.val:
                return helper(l.left, r.right) and helper(l.right, r.left)
            else:
                return False

        return helper(root.left, root.right)

'''
bfs
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        from collections import deque
        queue = deque([(root.left, root.right)])

        while queue:
            l, r = queue.popleft()
            if l and r:
                if l.val == r.val:
                    queue.append([l.left, r.right])
                    queue.append([l.right, r.left])
                else:
                    return False
            else:
                if not l and not r:
                    pass
                else:
                    return False

        return True





