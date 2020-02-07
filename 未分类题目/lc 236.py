#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/3 10:48
#@Author: LI Dongdong
#@File  : lc 236.py

# Definition for a Binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import copy
class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        path = []
        node_p_path = []
        node_q_path = []
        finish = 0
        self.preorder(root, p, path, node_p_path, finish)
        path = []
        finish = 0
        self.preorder(root, q, path, node_q_path, finish)
        path_len = 0
        node_p_path=copy.deepcopy(node_p_path[0])
        node_q_path=copy.deepcopy(node_q_path[0])
        if len(node_p_path) < len(node_q_path):
            path_len = len(node_p_path)
        else:
            path_len = len(node_q_path)
        result = TreeNode(0)
        for i in range(path_len):
            if node_p_path[i] == node_q_path[i]:
                result.val = node_p_path[i]
        return result

    def preorder(self, node, search, path, resultpath, finish):
        if not node or finish == 1:
            return
        path.append(node.val)
        if node.val == search.val:
            finish = 1
            resultpath.append(copy.deepcopy(path))
        self.preorder(node.left, search, path, resultpath, finish)
        self.preorder(node.right, search, path, resultpath, finish)
        path.pop()


a=TreeNode(3)
b=TreeNode(5)
c=TreeNode(1)
d=TreeNode(6)
e=TreeNode(2)
f=TreeNode(0)
x=TreeNode(8)
y=TreeNode(7)
z=TreeNode(4)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=x
e.left=y
e.right=z

x=Solution()
x.lowestCommonAncestor(a,b,f)