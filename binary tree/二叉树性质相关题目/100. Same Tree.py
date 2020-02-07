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
    traversal two trees, save them as lists tO(logN) sO(N)
    compare these two lists tO(N) sO(1)
time complex: 
space complex: 
易错点：
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        listP = self.transfer(p)  # transfer as list
        listQ = self.transfer(q)

        if listP == listQ:  # compare
            return True
        else:
            return False

    def transfer(self, treeNode):  # transfer tree as list
        if not treeNode:  # corner case
            return None

        self.transfer(treeNode.left)



