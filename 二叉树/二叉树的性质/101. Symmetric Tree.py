#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:20
# @Author  : LI Dongdong
# @FileName: 101. Symmetric Tree.py
''''''
'''
题目概述：
题目考点
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
返回值复杂形式
转变为 对两个树（子树）是否对称的判断
dfs return whether two subtree is symmetric
'''


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True

        def checkSub(r1, r2):  # return True or False， 先判断根，再得到左右，并判断左右
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False

            if r1.val == r2.val:
                l = checkSub(r1.left, r2.right)
                r = checkSub(r1.right, r2.left)
                return l and r
            else:
                return False

        return checkSub(root.left, root.right)


'''
遍历点模式的复杂模式
'''


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True

        self.res = True

        def scanNode(r1, r2):  # 先判断根，再判断左右
            if not r1 and not r2:
                return
            if not r1 or not r2:
                self.res = False
                return
            if r1.val == r2.val:
                scanNode(r1.left, r2.right)
                scanNode(r1.right, r2.left)
            else:
                self.res = False
            return

        scanNode(root.left, root.right)
        return self.res

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





