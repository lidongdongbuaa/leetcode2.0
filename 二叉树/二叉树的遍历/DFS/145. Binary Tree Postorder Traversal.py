#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 20:15
# @Author  : LI Dongdong
# @FileName: 145. Binary Tree Postorder Traversal.py
''''''
'''
题目分析
1.要求：
    Given a binary tree, return the postorder traversal of its nodes' values.
    
    Example:
    
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: 
    Follow up: Recursive solution is trivial, could you do it iteratively?
2.理解： post order the tree, output the node val in list
3.类型： binary tree
4.确认输入输出及边界条件：
    input： tree root with API, repeated? Y order? N value range? N
    output: list[int]
    corner case: 
        None -> []
        only one -> [int]
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
dfs from top to down
'''


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        res = []

        def dfs(root):  # scan every node
            if not root:  # base case
                return

            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

            return root

        dfs(root)

        return res


'''
dfs bottom up
'''


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        l = self.postorderTraversal(root.left)
        r = self.postorderTraversal(root.right)

        return l + r + [root.val]


'''
dfs iteration
'''


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]

