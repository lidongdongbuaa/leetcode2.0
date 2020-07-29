#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 7:14
# @Author  : LI Dongdong
# @FileName: 129. Sum Root to Leaf Numbers.py
''''''
'''
题目分析
1.要求：Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.
    
    Find the total sum of all root-to-leaf numbers.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
    Example 2:
    
    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
2.理解：find all path and get int by path and sum of them
3.类型：binary tree path
4.确认输入输出及边界条件：
    input:tree root with tree node API,  0 =<node value <= 9, node numb? N repeated? Y order? N
    output:int
    corner case: None -> 0, only one -> int

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''

'''
dfs from top to bottom
helper function dfs(root, path_val)
    if root is leaf, save path_val to self.res
return sum of self.res

time complexity: O(n)
space: O(n)
'''


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        self.res = 0

        def dfs(root, path_val):  # scan every node, save leaf path to res
            if not root:
                return

            if not root.left and not root.right:
                self.res += path_val

            if root.left:
                dfs(root.left, path_val * 10 + root.left.val)
            if root.right:
                dfs(root.right, path_val * 10 + root.right.val)
            return

        dfs(root, root.val)

        return self.res


'''
dfs iteration
first right
then left
'''


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        res = 0

        stack = [[root, root.val]]

        while stack:
            root, path_val = stack.pop()
            if not root.left and not root.right:
                res += path_val
            if root.right:
                stack.append([root.right, path_val * 10 + root.right.val])
            if root.left:
                stack.append([root.left, path_val * 10 + root.left.val])
        return res


'''
bfs 
'''


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        res = 0

        from collections import deque
        queue = deque([[root, root.val]])

        while queue:
            root, path_val = queue.popleft()
            if not root.left and not root.right:
                res += path_val
            if root.left:
                queue.append([root.left, path_val * 10 + root.left.val])
            if root.right:
                queue.append([root.right, path_val * 10 + root.right.val])
        return res