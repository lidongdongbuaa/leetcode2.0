#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 19:28
# @Author  : LI Dongdong
# @FileName: 94. Binary Tree Inorder Traversal.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
    
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: [1,3,2]
    Follow up: Recursive solution is trivial, could you do it iteratively?
2.理解：in-order to scan all node and save them in list
3.类型：binary tree
4.确认输入输出及边界条件：
    input: root with tree API, repeated? Y order? N value range? No range
    output: list[int]
    corner case: 
        None? -> []
        Only one - [int]
4.方法及方法分析：DFS - in order, iterative - 0/1 notation
time complexity order: DFS - in order O(N) =  iterative - 0/1 notation O(N)
space complexity order: DFS - in order O(logN) < iterative - 0/1 notation O(N)
'''

'''
dfs
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        res = []

        def dfs(root):  # inorder to scan every node
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

            return

        dfs(root)

        return res


'''
dfs from bottom to up
'''


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        l = self.inorderTraversal(root.left)
        r = self.inorderTraversal(root.right)

        return l + [root.val] + r


'''
dfs with stack
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        stack = []
        res = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()
            res.append(cur.val)

            if cur.right:
                root = cur.right
        return res
