#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 11:49
# @Author  : LI Dongdong
# @FileName: 450. Delete Node in a BST.py
''''''
'''
题目概述：删除二叉搜索树的节点x，返回根节点
题目考点：二叉搜索树的删除
解决方案：二分法确定为x值的node，然后分四种情况讨论node：node是leaf, node无左，node无右，node左右都有
方法及方法分析：recursion
time complexity order: O(logN)
space complexity order: O(logN)
如何考
易错点：不要写成helper函数（直接在tree上删除，无返回），因为root = root.right等是直接赋值的，导致原root的根本没变，
    故需要有返回值，return 返回后的头节点
'''
'''
delete the node in BST

input:
    tree root: None? Y; only one? N
    key: int; None?N; out of range of tree node? N
output:
    tree root

A. recursion： 
    Method:
        1. find the node with key val by binary search
        2. delete the node and replace it with its subtree node
            a. node is leaf, delete it directly
            b. node has the right child, use successor node replace it and delete the successor in rigth tree
            c. node has the left child, use predecessor node replace it and delete it in left tree
        3. return root

    Time complexity: O(logN) logN  is height of the tree
    Space: O(logN)
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:  # corner case
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # root.val == key
            if not root.left and not root.right:
                root = None
            elif root.right:
                successor = self.findSuc(root)
                root.val = successor
                root.right = self.deleteNode(root.right, successor)
            else:
                predecessor = self.findPre(root)
                root.val = predecessor
                root.left = self.deleteNode(root.left, predecessor)

        return root

    def findSuc(self, root):  # find the smallest node of root right subtree
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def findPre(self, root):  # find the biggest node of root left subtree
        root = root.left
        while root.right:
            root = root.right
        return root.val


'''
B. recursion： 
    Method:
        1. find the node with key val by binary search
        2. delete the node and replace it with its subtree node
            a. node is leaf, delete it directly
            b. node have only left child, use left child replace the node
            c. node have only right child, use right child replace it
            d. node has left and right, use the successor/predecessor node replace it
        3. return root
    
    
    Time complexity: O(logN) logN  is height of the tree
    Space: O(logN)
'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:  # corner case
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # root.val == key
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root.val = self.findSuc(root)
                root.right = self.deleteNode(root.right, root.val)
        return root

    def findSuc(self, root):  # find the smallest node of root right subtree
        root = root.right
        while root.left:
            root = root.left
        return root.val