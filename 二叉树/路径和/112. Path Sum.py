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
A. pre-order traversal 
Method: 
    main() corner case,  + return help()
    help(root, sum, tmp) use pre-order traversal to scan every path node, add the node value
        if add result = sum, return True
    after traversal, reduce the last node value
time complex: O(N) visit every node
space complex: O(logN) average case
易错点：
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:  # corner case
            return False

        tmp = 0
        return self.dfs(root, sum, tmp)

    def dfs(self, root, target, tmp):  # output: T/F
        if not root:  # corner case
            return False

        tmp += root.val
        if not root.left and not root.right:  # root is leaf
            if tmp == target:
                return True


        l = self.dfs(root.left, target, tmp)
        r = self.dfs(root.right, target, tmp)
        return l or r
        tmp -= root.val

'''
B. iterative method using stack
Method: 
    traversal the nodes by stack to simulate the recursion
        accumulate the node value
            if == sum, return True
            else: reduce current node value
time complex: O(N)
space complex: O(logN)
易错点：类似BFS中的queue.append([root, 0])
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:  # corner case
            return False

        stack = [[root, root.val]]
        while stack:
            root, tmp = stack.pop()
            if root.right:
                stack.append([root.right, tmp + root.right.val])
            if root.left:
                stack.append([root.left, tmp + root.left.val])

            if not root.left and not root.right and tmp == sum:
                return True
        return False

'''
C.BFS
    Method:
        deque to save root and the value
            deque pop the left node, the value 
            deque add node's left/right node and added value
            if node is leaf and value == target, return
        return False
    time O(N) space O(N)
    
'''
from collections import deque
class Solution:
    def hasPathSum(self, root, sum):  # return T/F
        if not root:  # corner case
            return False

        queue = deque([(root, root.val)])

        while queue:
            root, value = queue.popleft()
            if not root.left and not root.right and value == sum:
                return True
            if root.left:
                queue.append([root.left, value + root.left.val])
            if root.right:
                queue.append([root.right, value + root.right.val])

        return False
