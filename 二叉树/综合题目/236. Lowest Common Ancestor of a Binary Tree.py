#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 21:39
# @Author  : LI Dongdong
# @FileName: 236. Lowest Common Ancestor of a Binary Tree.py
''''''
'''
题目概述：求两个树中节点的最近公共祖先
题目考点：bottom-up 的recursion方法
解决方案：dfs(root) return true if root tree have p or q, then judge l + r + mid condition
方法及方法分析：递归法；
time complexity order: 
space complexity order: 
如何考
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
dfs check p or q in the tree of node
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:  # base case
            return None

        self.res = None

        def dfs(root):  # return true is p or q in root
            if not root:
                return False

            l = dfs(root.left)
            r = dfs(root.right)

            if l and r:  # left and right has p and q
                self.res = root
                return
            if (l or r) and (root.val == p.val or root.val == q.val):  # root has p or q and l or r has p or q
                self.res = root
                return


            if (root.val == p.val or root.val == q.val) or l or r:
                return True

            return False

        dfs(root)
        return self.res



