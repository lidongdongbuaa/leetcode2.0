#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 17:15
# @Author  : LI Dongdong
# @FileName: Count Visible Nodes in Binary Tree.py
''''''
'''
题目概述：在二叉树中，有一种node，从root到node的所有点都小于等于node，统计这样node的数量
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

corner case:
    1. root is None:
    2. only one root

Method：
    1. 统计所有路径, 保存到list
    2. 对每个list，统计符合要求的点的个数
'''
class Tree:
    def countNumb(self, root):  # return int

        def count(root, base):  # return int
            if not root:
                return 0

            count = 0
            if root.val >= base:
                count += 1
                base = root.val

            return count + count(root.left, base) + count(root.right, base)

        return count(root, float('-inf'))