#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 17:31
# @Author  : LI Dongdong
# @FileName: 700. Search in a Binary Search Tree.py
''''''
'''
题目概述：在BST中寻找值为key的node，并返回其及其所在的树
题目考点：BST的二分搜索
解决方案：迭代和递归模拟二分搜索
方法及方法分析：迭代和递归
time complexity order: 迭代 = 递归 O(logN)
space complexity order: 迭代 O(1) < 递归O(logN)
如何考
'''
'''
find a node which has val
like binary searh 

input: tree root node; None? Y; tree is binary search tree? Y
    val: int; value range to the tree? in or out of range of tree
output: tree node with subtree / None
corner case:
    root is None -> None
    val is None -> None

A.iterative - like binary search 
    Method:
        1. corner case
        2. compare val with root val
            if <, root = root.left
            if > root = root.right
            else: return root

    Time: O(logN) N is number of tree
    Space: O(1)

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:  # corner case
            return None
        if val is None:
            return None

        while root:
            if val < root.val:
                root = root.left
            elif val == root.val:
                return root
            else:
                root = root.right
        return None


'''
B. recursion
    Method:
        1. end: root.val = val, return root
        2. Process, if val < root value, search left subtree
            else, search right subtree
    Time O(logN)
    Space O(logN)

'''


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:  # corner case
            return None
        if val is None:
            return None
        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)