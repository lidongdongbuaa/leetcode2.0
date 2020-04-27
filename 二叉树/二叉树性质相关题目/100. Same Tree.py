#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 9:55
# @Author  : LI Dongdong
# @FileName: 100. Same Tree.py
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
corner case
    one is None
    both are None

思路：分治；一边遍历，一边比对

A. pre-order scan
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val == q.val:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            if l == True and r == True:
                return True
            else:
                return False
        else:
            return False
'''
B. level order scan
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        from collections import deque
        queue = deque([(p, q)])

        while queue:
            p, q = queue.popleft()
            if q and p:
                if q.val == p.val:
                    queue.append([q.left, p.left])
                    queue.append([q.right, p.right])
                else:
                    return False
            else:
                if not q and not p:
                    pass
                else:
                    return False
        return True



