#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 16:48
# @Author  : LI Dongdong
# @FileName: 98. Validate 二分搜索 Tree.py
''''''
'''
题目概述：判断一个树是否是BST
题目考点：BST中序遍历是单调递增的；树的中序遍历的迭代方法；分治思想的递归
解决方案：分治递归判断root与parent值的关系；中序遍历迭代法，与pre_node val进行对比
方法及方法分析：recursion; in-order iteration
time complexity order: O(N)
space complexity order: O(H) = O(logN)
如何考
'''
'''
check if a tree is BST

input: tree node; None? N
output: True or False
corner case:
    root is None -> True

A. recursion - left < root < right,因为节点不仅依靠自身，也依靠子树的节点进行判断，故需要把子树的节点值放入变量中，才可以满足层层处理的递归思想
    Method:
        if root 最底层情况，corner case,即搜索到底层情况后，返回什么
        elif root 不是底层情况
            判定root - 通过输入的变量进行比对
                若成立，判定其左右 helper(root.left) 和 helper(root.right)
                不成立，返回False

    Time: O(N), N is number of the nodes
    Space: O(H),H is height of the tree, average is O(logN)
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True  # 若题目要求 root is None 时，返回False，则在此处改为False，helper()中的不变，依然是return True

        def helper(root, low, upper):  # return T or F for check
            if not root:  # 触底时，返回
                return True
            else:
                if low < root.val < upper:
                    return helper(root.left, low, root.val) and helper(root.right, root.val, upper)
                else:
                    return False

        return helper(root, float('-inf'), float('inf'))


'''
C. inorder iterative traversal method - the node value is increasing, and stack simulating the recursion
    Method:
        1. corner case
        2. iteratively inorder traversal the node, compare the node value with its left node value
            if current node value < left node value, return False
        3.return True
    Time: O(N)
    Space: O(H), average is logN
易错点：
    在判断有right之后，不是stack加入右点，而是p_node指向右点

'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        stack = []
        p_node = root
        pre_val = float('-inf')
        while stack or p_node:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            cur_node = stack.pop()
            if pre_val >= cur_node.val:
                return False
            else:
                pre_val = cur_node.val

            if cur_node.right:
                p_node = cur_node.right
        return True




