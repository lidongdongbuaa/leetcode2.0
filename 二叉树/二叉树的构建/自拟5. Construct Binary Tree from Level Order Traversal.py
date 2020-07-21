# -*- coding: utf-8 -*-
# @Time    : 2/11/2020 11:44 AM
# @Author  : LI Dongdong
# @FileName: Construt Binary Tree from Level Order Traversal.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
input: list, length range is from 0 to inf; value range no limit; level order; have repeated
output: root tree node
corner case: 
    list is None, return None

construct full binary tree

Method1 level order to build the tree
use bfs to create the tree
    use deque([root, index]}, index is for the list to search the value
Time complexity: O(n)
Space: O(1)
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructTree(self, nodeList):  # input: list using bfs, output: root
        if not nodeList:  # corner case
            return None

        res = root = TreeNode(nodeList[0])
        n = len(nodeList)

        from collections import deque
        queue = deque([(root, 0)])

        while queue:
            root, index = queue.popleft()
            if 2 * index <= n - 1:
                root.left = TreeNode(nodeList[2 * index])
                queue.append([root.left, 2 * index])
            if 2 * index + 1 <= n - 1:
                root.right = TreeNode(nodeList[2 * index + 1])
                queue.append([root.right, 2 * index + 1])

        return res
