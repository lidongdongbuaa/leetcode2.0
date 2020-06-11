#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:20
# @Author  : LI Dongdong
# @FileName: 101. Symmetric Tree.py
''''''
'''
题目概述：判断树是否对称
题目考点：转化为判断两个树是否对称；
优化核心：
易错点：
方法及方法分析：四种方法
time complexity order: O(N)
space complexity order: O(logN)
如何考
'''
'''
check the tree -> check the subtrees are symmetirc
dfs 自下而上
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True
        if not root.left and not root.right:
            return True

        def dfs(r1, r2):  # check r1 and r2 symmetric
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            else:
                l = dfs(r1.left, r2.right)
                r = dfs(r1.right, r2.left)
                return l and r

        return dfs(root.left, root.right)

'''
dfs自上而下
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        self.res = True
        def dfs(r1, r2):  # scan every node
            if not r1 and not r2:
                return
            if not r1 or not r2:
                self.res = False
                return
            if r1.val != r2.val:
                self.res = False
                return
            dfs(r1.left, r2.right)
            dfs(r1.right, r2.left)
            return

        dfs(root.left, root.right)
        return self.res

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        stack = [(root.left, root.right)]
        while stack:
            r1, r2 = stack.pop()
            if not r1 and not r2:
                pass
            elif not r1 or not r2:
                return False
            elif r1.val != r2.val:
                return False
            else:  # r1.val == r2.val
                stack.append([r1.left, r2.right])
                stack.append([r1.right, r2.left])
        return True

'''
bfs
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        from collections import deque
        queue = deque([(root.left, root.right)])

        while queue:
            r1, r2 = queue.popleft()
            if not r1 and not r2:
                pass
            elif not r1 or not r2:
                return False
            elif r1.val != r2.val:
                return False
            else:
                queue.append([r1.left, r2.right])
                queue.append([r1.right, r2.left])
        return True





