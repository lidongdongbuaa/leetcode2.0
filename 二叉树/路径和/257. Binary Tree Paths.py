#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 16:16
# @Author  : LI Dongdong
# @FileName: 257. Binary Tree Paths.py
''''''
'''
题目分析
1.要求：Given a binary tree, return all root-to-leaf paths.

    Note: A leaf is a node with no children.
    
    Example:
    
    Input:
    
       1
     /   \
    2     3
     \
      5
    
    Output: ["1->2->5", "1->3"]
    
    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
2.理解：scan all tree node and return string with ->
3.类型：binary tree path
4.确认输入输出及边界条件：
    input: tree root node with definition, the node's value range? N, number of node? N, repeated? Y ordered? N
    output: list[string]
    corner case:
        None：[]
5.方法及方法分析：DFS, BFS
time complexity order: O(N)
space complexity order: O(N)
6.如何考: 没法考oa
'''
'''
dfs from top to bottom
time complexity: O(n)
space:O(n) skewed tree

dfs(root, path)
'''


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:  # corner case
            return []

        self.res = []

        def dfs(root, path):  # scan every node and save leaf path to res
            if not root:  # base case
                return

            if not root.left and not root.right:
                self.res.append(path[:])

            if root.left:
                dfs(root.left, path + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, path + '->' + str(root.right.val))

            return

        dfs(root, str(root.val))

        return self.res


'''
dfs iteration
right - left
'''


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:  # corner case
            return []

        res = []

        stack = [[root, str(root.val)]]

        while stack:
            root, path = stack.pop()
            if not root.left and not root.right:
                res.append(path[:])
            if root.right:
                stack.append([root.right, path + '->' + str(root.right.val)])
            if root.left:
                stack.append([root.left, path + '->' + str(root.left.val)])
        return res


'''
bfs 
'''


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:  # corner case
            return []

        res = []

        from collections import deque
        queue = deque([[root, str(root.val)]])

        while queue:
            root, path = queue.popleft()
            if not root.left and not root.right:
                res.append(path[:])
            if root.left:
                queue.append([root.left, path + '->' + str(root.left.val)])
            if root.right:
                queue.append([root.right, path + '->' + str(root.right.val)])
        return res
