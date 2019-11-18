#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/16 22:26
# @Author  : LI Dongdong
# @FileName: 112. Path Sum.py
''''''
'''
题目分析
1.要求：Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
    such that adding up all the values along the path equals the given sum.
    A leaf is a node with no children.
2.理解：二叉树前序遍历
3.类型：二叉树前序遍历
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
recursion method
idea：use preorder traverse to find the path
edge case：root is None
method：
    use recursion to traverse the tree: node_list #tO(logN) sO(N)
    cumulate node val until node is leaf. judge total of node val is sum
    pop the last node and continue cumulation
time complex: O(logN)
space complex: O(N)
易错点：
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return
        self.sum += root.val
        if root.left is None and root.right is None and self.sum == sum:
            return True
        self.hasPathSum(root.left, sum)
        self.hasPathSum(root.right, sum)
        self.sum -= root.val


'''
test case
'''
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(11)
d = TreeNode(7)
e = TreeNode(2)
f = TreeNode(8)
g = TreeNode(13)
h = TreeNode(4)
i = TreeNode(1)

a.left = b
a.right = f
b.left = c
c.left = d
c.right = e
f.left = g
f.right = h
h.right = i

x = Solution()
x.hasPathSum(a, 22)
