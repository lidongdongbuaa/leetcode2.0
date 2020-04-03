#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 21:39
# @Author  : LI Dongdong
# @FileName: 236. Lowest Common Ancestor of a Binary Tree.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Method:
    1. corner case
    2. find a path including p and a path including q, save them in list1, and list2
        3-5-6, 3-1-0
    3. traversal the list1 and list2 at same time from the begining, if find the last common node is the res
        3 is result
优化点:
    判断path有了target，用root.val == target.val,而不用target.val in path，这样时间复杂度从O(N) - O(1)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        list1 = []
        list2 = []

        self.findPath(root, [], list1, p, 0)
        self.findPath(root, [], list2, q, 0)

        list1 = list1[0]
        list2 = list2[0]

        i = 0
        length = min(len(list1), len(list2))
        for i in range(length):
            if list1[i] == list2[i]:
                res = list1[i]
        return TreeNode(res)


    def findPath(self, root, path, res, target, finish):  # find a path including target and save it in res
        if not root or finish == 1:
            return

        path.append(root.val)
        if root.val == target.val:
            res.append(path[:])
            finish = 1
        self.findPath(root.left, path, res, target, finish)
        self.findPath(root.right, path, res, target, finish)
        path.pop()
