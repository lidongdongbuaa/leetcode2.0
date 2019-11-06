#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/6 14:16
#@Author: LI Dongdong
#@File  : lc 114.py
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root) :
        """
        Do not return anything, modify root in-place instead.
        """
        last = None
        self.preorder(root, last)
        result=[]
        while root:
            result.append(root.val)
            root=root.right
        print(result)

    def preorder(self, node, last):
        if not node:
            return
        if node.left == None and node.right == None:
            last = node
            return
        left = node.left
        right = node.right
        left_last = None
        right_last = None
        if left:
            self.preorder(left, left_last)
            node.left = None
            node.right = left
            last = left_last
        if right:
            self.preorder(right, right_last)
            if left_last:
                left_last.right = right
            last = right_last



a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(5)
d=TreeNode(3)
e=TreeNode(4)
f=TreeNode(6)
a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

x=Solution()
x.flatten(a)