#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 16:20
# @Author  : LI Dongdong
# @FileName: 669. Trim a 二分搜索 Tree.py
''''''
'''
题目概述：在给定值的范围内，trim修剪一个BST
题目考点：从上到下进行划分
解决方案：递归，设想trim()是已经trim好的，对比LR与root，划定范围-> 类似于二分法里找一定范围内的值
方法及方法分析：递归
time complexity order: O(N) worst case, skewed tree
space complexity order: O(N) worst case
如何考
'''
'''
trim the tree node to [L, R]

input:
    tree root: None? Y;
    L, R; value range? L <= R, L, R may out of tree node value range;
output:
    tree root node
corner case:
    tree root is None -> None

A. recursion - 把trim(node.left/right)假设为在node的子树上的理想答案
    Method:
        1. end: root is None
        2. if R is less than root val, return search result of left subtree, 缩小范围
        3. if L is more than root val, return search result of right subtree， 缩小范围
        4. if L <= root val and R >= root.val，trim both sides of the tree
 
    Time: O(N), visit each node at most once
    Space: O(N), the call stack of our recursion could be as large as the number of nodes in the worst case.
易错点：本题可以很好的处理L，R超过tree界限的问题，会返回None或者原root
易错点：
    先base case，后自上而下的缩小范围，把函数当作已经完成的
    在root小于左边界时，应该保留root的right继续进行运算
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None

        if R < root.val:
            return self.trimBST(root.left, L, R)
        elif root.val < L:  # 变相的'删除'掉了当前root和所有root.left的node
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root  # 返回给parent一个区间调整完以后的subtree
