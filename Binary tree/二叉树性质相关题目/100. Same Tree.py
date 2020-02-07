#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 9:55
# @Author  : LI Dongdong
# @FileName: 100. Same Tree.py
''''''
'''
题目分析
1.要求：Given two binary trees, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
2.理解：judge whether two binary trees are same
3.类型：BT
4.确认输入输出及边界条件：
    input: repeated value? Y ordered? N node val range? None
    output: True or False
    corner case: None? N one only node? N
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force
方法：
    traversal two trees, save them as lists tO(N) sO(N)
    compare these two lists tO(N) sO(1)
time complex: tO(N)
space complex: sO(N)
易错点：
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        data = []
        listP = self.transfer(p, data)  # transfer as list
        data = []
        listQ = self.transfer(q, data)

        if listP == listQ:  # compare
            return True
        else:
            return False

    def transfer(self, treeNode, data):  # transfer tree as list
        if not treeNode:  # corner case
            return data.append(None)

        data.append(treeNode.val)
        self.transfer(treeNode.left, data)
        self.transfer(treeNode.right, data)
        return data


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
a.left = b
# a.right = c

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(2)
# a.left = b
a1.right = c1

X = Solution()
data = []
print(X.isSameTree(a, a1))

'''
思路：compare node directly
方法：
    recursive the tree, compare every node
time complex: tO(N)
space complex: sO(1)
易错点：
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True

        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True


'Optimized code'
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
