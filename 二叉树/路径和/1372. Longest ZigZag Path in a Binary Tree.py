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

'''
dfs from bottom to up
helper function dfs(root), return max left length and max right length
    renew self.res
'''


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        self.res = 0

        def dfs(root):  # scan evey node, return max left lenght and max right length
            if not root:
                return -1, -1

            l_l, l_r = dfs(root.left)
            r_l, r_r = dfs(root.right)

            self.res = max(self.res, l_r + 1, r_l + 1)

            return l_r + 1, r_l + 1

        dfs(root)

        return self.res


'''
dfs from up to bottom 
self.res
dfs(root, left path, right path)
    renew res by left path and right path
'''


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        self.res = 0

        def dfs(root, l, r):  # scan every node
            if not root:  # base case
                return

            self.res = max(self.res, l, r)

            dfs(root.left, 0, l + 1)
            dfs(root.right, r + 1, 0)
            return

        dfs(root, 0, 0)

        return self.res


'''
dfs from up to bottom iteration
'''


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        res = 0

        stack = [[root, 0, 0]]

        while stack:
            root, l, r = stack.pop()
            res = max(res, l, r)
            if root.right:
                stack.append([root.right, r + 1, 0])
            if root.left:
                stack.append([root.left, 0, l + 1])

        return res


'''
bfs 
'''


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        res = 0

        from collections import deque
        queue = deque([[root, 0, 0]])

        while queue:
            root, l, r = queue.popleft()
            res = max(res, l, r)
            if root.left:
                queue.append([root.left, 0, l + 1])
            if root.right:
                queue.append([root.right, r + 1, 0])

        return res
