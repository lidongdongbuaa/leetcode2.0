#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 21:45
# @Author  : LI Dongdong
# @FileName: 112. Path Sum.py
''''''
'''
题目分析
1.要求：Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

    Note: A leaf is a node with no children.
    
    Example:
    
    Given the below binary tree and sum = 22,
    
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
2.理解：judge there is a path equal to sum
3.类型：binary tree
4.确认输入输出及边界条件：
    input:root with tree API, sum: int, tree node, repeated? Y, order? N value range? >0 number range? N, sum range? >0
    output:True or False
    corner case: root None? -> False
4.方法及方法分析： pre-order DFS, iterative DFS, BFS
time complexity order: O(N)
space complexity order: 
'''

'''
input: tree root; length range is from 0 to inf; node value range is no limit; 
output: True/False
corner case
    root is None, return False

dfs from up to down
corner case
helper function dfs(root, node sum)
    use preorder traverse every node
    if node is leaf and node sum == sum, self.res = True
return self.res

Time complexity: O(n)
Space: O(n), in worst case, tree height is n
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:  # corner case
            return False

        self.res = False

        def dfs(root, node_sum):  # traverse tree node
            if not root:
                return

            if not root.left and not root.right and node_sum == sum:
                self.res = True
                return

            if root.left:
                dfs(root.left, node_sum + root.left.val)
            if root.right:
                dfs(root.right, node_sum + root.right.val)
            return

        dfs(root, root.val)

        return self.res


'''
dfs using iteration preorder
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:  # corner case
            return False

        stack = [(root, root.val)]

        while stack:
            root, node_sum = stack.pop()
            if not root.left and not root.right and node_sum == sum:
                return True
            if root.right:
                stack.append([root.right, node_sum + root.right.val])
            if root.left:
                stack.append([root.left, node_sum + root.left.val])
        return False


'''
bfs
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:  # corner case
            return False

        from collections import deque

        queue = deque([(root, root.val)])

        while queue:
            root, node_sum = queue.popleft()
            if not root.right and not root.left and node_sum == sum:
                return True
            if root.left:
                queue.append([root.left, node_sum + root.left.val])
            if root.right:
                queue.append([root.right, node_sum + root.right.val])
        return False

