#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 19:08
# @Author  : LI Dongdong
# @FileName: 113. Path Sum II.py
''''''
'''
题目分析
1.要求：Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    Note: A leaf is a node with no children.
    
    Example:
    
    Given the below binary tree and sum = 22,
    
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    Return:
    
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
2.理解：find all path whose sum = sum, return them is list
3.类型：binary tree path sum
4.确认输入输出及边界条件：
    input:root with tree node API, node val repeated? Y order? N value range? N node numb? N
    output: list[[]]
    corner case: None?-> [], Only one? ->[[node.val]]

5.方法及方法分析：preoder traveral and store, iterative method by stack simulating recursion
time complexity order: 
space complexity order: 
6.如何考？
'''
'''
dfs with helper function
corner case
create dfs(root, node_list, node_sum)
    if root is leaf, save node_list to res
run dfs
return res

time complexity: O(n*2)
space: O(n) if the tree is skewed
'''


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:  # corner case
            return []

        self.res = []

        def dfs(root, node_list, node_sum):  # scan all node and save res candidates in res
            if not root:  # base case
                return

            if not root.left and not root.right and node_sum == sum:
                self.res.append(node_list[:])

            if root.left:
                dfs(root.left, node_list + [root.left.val], node_sum + root.left.val)
            if root.right:
                dfs(root.right, node_list + [root.right.val], node_sum + root.right.val)
            return

        dfs(root, [root.val], root.val)
        return self.res


'''
dfs iteration
'''


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:  # base case
            return []

        stack = [[root, [root.val], root.val]]

        res = []

        while stack:
            root, node_list, node_sum = stack.pop()
            if not root.left and not root.right and node_sum == sum:
                res.append(node_list[:])
            if root.right:
                stack.append([root.right, node_list + [root.right.val], node_sum + root.right.val])
            if root.left:
                stack.append([root.left, node_list + [root.left.val], node_sum + root.left.val])
        return res


'''
bfs
'''


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:  # base case
            return []

        from collections import deque
        queue = deque([[root, [root.val], root.val]])

        res = []

        while queue:
            root, node_list, node_sum = queue.popleft()
            if not root.left and not root.right and node_sum == sum:
                res.append(node_list[:])
            if root.left:
                queue.append([root.left, node_list + [root.left.val], node_sum + root.left.val])
            if root.right:
                queue.append([root.right, node_list + [root.right.val], node_sum + root.right.val])
        return res