#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 9:33
# @Author  : LI Dongdong
# @FileName: 701. Insert into a 二分搜索 Tree.py
''''''
'''
题目概述：在bst中插入节点
题目考点：bst的插入的递归和迭代方法； 备份root
解决方案：递归法； 迭代法，在position为None处加入点
方法及方法分析：递归；迭代
time complexity order: O(H = logN)
space complexity order: 迭代 O(1) <  递归O(H)
如何考
'''
'''
input:
    tree root: None? Y only one? Y; BST
    value: value range? not in the tree
output:
    root node
corner case:
    root is None: -> listNode(value)

A. recursion
    Method:
        1. End: root is None, return ListNode(value)
        2. if value < root.val, do it on left substree, return root
        3. if value > root.val, do it on right subtree, return root

    Time: O(H), H is height of tree, for perfect tree, height is logN N is numnber of node
    Space: O(H)

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


'''
B. iterative  -> find None position and add the node
    Method:
        1. corner case
        2. save root as res, and find the position of val in tree by binary search
        3. add the val as leaf

    Time: O(H), H is height of tree, for perfect tree, height is logN N is numnber of node
    Space: O(1)

'''


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:  # corner case
            return TreeNode(val)

        cur = root
        while cur:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    return root
                else:
                    cur = cur.right

