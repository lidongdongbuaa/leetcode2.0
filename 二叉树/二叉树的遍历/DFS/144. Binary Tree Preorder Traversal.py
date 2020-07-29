#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 16:50
# @Author  : LI Dongdong
# @FileName: 144. Binary Tree Preorder Traversal.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the preorder traversal of its nodes' values.
    Example:
    
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: [1,2,3]
    Follow up: Recursive solution is trivial, could you do it iteratively?
2.理解：前序遍历， 手工栈模拟递归
3.类型：DFS
4.确认输入输出及边界条件：
    input: root of tree, with API of tree, value range? No
    output: list
    corner case: None? -> None Only one? -> [int]
4.方法及方法分析：DFS, iterative - Color notation stack to simulate recursion
time complexity order: DFS O(N) = stack to simulate recursion O(N) = interative - color notation O(N)
space complexity order:  DFS O(logN) < stack to simulate recursion O(N) =  interative - color notation O(N)
'''
'''
dfs from up to down
'''


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        res = []

        def dfs(root):  # scan every node
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)

        return res


'''
dfs bottom-up
'''


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        l = self.preorderTraversal(root.left)
        r = self.preorderTraversal(root.right)

        return [root.val] + l + r


'''
dfs iteration
'''


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]

        res = []

        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return res