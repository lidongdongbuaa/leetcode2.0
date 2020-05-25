#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 19:58
# @Author  : LI Dongdong
# @FileName: 1372. Longest ZigZag Path in a Binary Tree.py
''''''
'''
题目分析
1.要求：最长z字形路径的长度
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
output: int, the zigzag path
corner case
    root is None, return -1
    root is only one node, return 0

dfs - return the left and right longest path
'''
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return -1
        if not root.left and not root.right:
            return 0

        self.res = 0

        def dfs(root):  # return left and right longest zigzag path
            if not root:
                return -1, -1

            leftL, leftR = dfs(root.left)
            rightL, rightR = dfs(root.right)
            cur = max(leftR, rightL) + 1
            self.res = max(self.res, cur)
            return leftR + 1, rightL + 1

        dfs(root)
        return self.res

'''
多参数方法
'''
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return -1
        if not root.left and not root.right:
            return 0

        self.res = 0

        def dfs(root, l, r):  # the path length from up to root in left l, in right r
            if not root:
                return

            self.res = max(self.res, l, r)
            if root.left:
                dfs(root.left, 0, l + 1)
            if root.right:
                dfs(root.right, r + 1, 0)
            return

        dfs(root, 0, 0)
        return self.res


'''
bfs
steps:
1. queue = [root, l, r], reach root, the longest path from left or right
2. pop node from queue, renew the res
3. push root.left and root.right into the queue
4. return the res
Time complexity: O(n)
Space: O(1)
'''


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return -1
        if not root.left and not root.right:
            return 0

        from collections import deque
        queue = deque([(root, 0, 0)])

        res = 0
        while queue:
            root, l, r = queue.popleft()
            res = max(res, l, r)
            if root.left:
                queue.append([root.left, 0, l + 1])
            if root.right:
                queue.append([root.right, r + 1, 0])
        return res