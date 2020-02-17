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
思路：brute force - All node and min one
方法：
    DFS to scan all node, get all path height
    find min path
time complex: O(N)
space complex: O(logN)
易错点
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = 0
        res = []
        self.depth(root, height, res)

        return min(res)

    def depth(self, root, height, res):  # root, res:List
        if not root:
            return

        if not root.left and not root.right:
            height += 1
            res.append(height)

        self.depth(root.left, height + 1, res)
        self.depth(root.right, height + 1,  res)

'''
B.
思路：DFS
方法：
    replace the res-list with res - int
time complex: O(N)
space complex: O(logN)
易错点：
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = 0
        res = float('inf')
        res = self.depth(root, height, res)

        return res

    def depth(self, root, height, res):  # root, res:List
        if not root:
            return res

        if not root.left and not root.right:
            height += 1
            res = min(height, res)


        res = self.depth(root.left, height + 1, res)
        res = self.depth(root.right, height + 1, res)
        return res
'''
C.
思路：DFS directly
方法：
    use DFS to scan the every node, and accumulate the min height
        case 1: not root
        case 2: root is leaf
        case 3 : root has only one branch
        case 4: case has two branch

'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:  # root is leaf
            return 1

        if not root.left or not root.right: # root is single branch node
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))

        if root.left and root.right:  # root is node having two branch
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

'''
D.
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


