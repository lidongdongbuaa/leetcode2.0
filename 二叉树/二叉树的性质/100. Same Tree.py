#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 9:55
# @Author  : LI Dongdong
# @FileName: 100. Same Tree.py
''''''
'''
题目概述：给定两个tree root，判定这两个tree是否相同
题目考点：多个tree的同时遍历
解决方案：dfs返回值；bfs
方法及方法分析：
time complexity order: O(n)
space complexity order: dfs:O(logN); bfs:O(N)
如何考
'''
'''
corner case
    one is None
    both are None
dfs 返回值基本形式
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
            return l and r
        else:
            return False
'''
dfs 参数基本形式
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        self.res = True

        def dfs(p, q):
            if not p and not q:
                return
            if not p or not q:
                self.res = False
                return
            if p.val != q.val:
                self.res = False
                return
            dfs(p.left, q.left)
            dfs(p.right, q.right)
            return

        dfs(p, q)
        return self.res

'''
dfs by iteration <--> dfs 无返回基本形式
use the stack to simulate recursion
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        stack = [(p, q)]
        while stack:
            r1, r2 = stack.pop()
            if r1 and r2:
                stack.append([r1.right, r2.right])
                stack.append([r1.left, r2.left])
                if r1.val != r2.val:
                    return False
            else:
                if not r1 and not r2:
                    pass
                else:
                    return False
        return True
'''
bfs
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



