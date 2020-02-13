#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 13:55
# @Author  : LI Dongdong
# @FileName: 111. Minimum Depth of Binary Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Given binary tree [3,9,20,null,null,15,7],
    
        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.
2.理解：find the minimal path length
3.类型: binary tree
4.确认输入输出及边界条件：
    input: root with definition, no range node val, repeated? Y, order？ N
    output：int
    corner case：
        None： 0
        Only one: 1
4.方法及方法分析：dfs, bfs
time complexity order: dfs O(N) = bfs O(N)
space complexity order: dfs O(logN) < bfs O(N)
'''
'''
A.
思路：dfs
方法：
    dfs to get left and right node height by dfs
        ending condition： 
            1. root == None
            2. root is leaf
            3. root is skewed
            4. root is balanced
    get the minimal height
time complex: O(N)
space complex: O(logN)
易错点：搞清楚递归结束条件, 递归就是多种情况下的分类
    return self.minDepth(root.right) + 1 # 1 代表目前的node的层，要加1
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if root.left and not root.right:
            return self.minDepth(root.left) + 1

        height_left = self.minDepth(root.left)
        height_right = self.minDepth(root.right)
        if root.left and root.right:
            return min(height_left, height_right) + 1

'''
optimized code
把skewed root的两种情况进行合并
原因：简化code
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        if not root.left or not root.right: # root is skewed
            return max(self.minDepth(root.right), self.minDepth(root.left)) + 1

        if root.left and root.right:
            height_left = self.minDepth(root.left)
            height_right = self.minDepth(root.right)
            return min(height_left, height_right) + 1

'''
B.
思路：bfs
方法：
    use deque to save [node, height]
    when meet leaf, return height
    push the node's l/r, add height
time complex: O(N)
space complex: O(N)
易错点：在第一次到达leaf时，立马return height
'''
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        queue = deque()
        queue.append([root, 1])

        while queue:
            node, height = queue.popleft()
            if not node.left and not node.right:
                return height
            if node.left:
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])

'''
test code
root = [1, 2, 3, None, None, 4]
queue [1,1]
node = 1, h = 1
queue [2,2] [3, 2]
node = 2, h = 2
return 2
'''


