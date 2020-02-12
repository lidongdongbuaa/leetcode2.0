# -*- coding: utf-8 -*-
# @Time    : 2/12/2020 11:25 AM
# @Author  : LI Dongdong
# @FileName: 104. Maximum Depth of Binary Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Given binary tree [3,9,20,null,null,15,7],
    
        3
       / \
      9  20
        /  \
       15   7
    return its depth = 3.
2.理解：calculate the height of root, and return longest
3.类型：binary tree
4.确认输入输出及边界条件：
    input: root with definition, range? No, repeated? N order? N
    output: int
    corner case：
        None? -> 0
        only one? -> 0
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：DFS
方法：
    dfs to scan node, meet leaf to record height
    compare the height to find the biggest one
time complex: O(N)
space complex: worst O(N), average O(logN)
易错点： 辅助函数用不到
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        if not root.left and not root.right: # corner case
            return 1

        length = 0
        length = self.findLength(root, length)  # find longest height
        return length

    def findLength(self, root, length):  # input: root, output: int
            if not root:  # corner case
                return 0
            if not root.right and not root.left:  # corner case
                return 1

            length = 1 + max(self.findLength(root.left, length), self.findLength(root.right, length))
            return length

'''
optimized Code
优化掉辅助函数findLenght
原因：length 没有起到作用
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        if not root.left and not root.right: # corner case
            return 1

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # get the longest one by dfs

'''
B.
思路：BFS
方法：
    
time complex: O(N)
space complex: 
易错点： 基本上都是在 queue.append([root, 1]) 做工作
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        queue = deque()
        queue.append([root, 0])
        max_depth = 0

        while queue:  # bfs scan and record
            node, height = queue.popleft()
            if not node.left and not node.right:  # must have subtree, it can add one
                height += 1
                max_depth = max(height, max_depth)
            if node.left:
                queue.append([node.left, height])
            if node.right:
                queue.append([node.right, height])
        return height



