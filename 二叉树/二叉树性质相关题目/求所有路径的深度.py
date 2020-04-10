#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 16:51
# @Author  : LI Dongdong
# @FileName: 求所有路径的深度.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：DFS
方法：
    scan all nodes by DFS, renew height, save height of leaf in res
        break case: root is None, root is leaf
        trigger: other case
time complex: 
space complex: 
易错点：
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = 0
        res = []
        self.depth(root, height, res)
        return res

    def depth(self, root, height, res):  # root, res:List
        if not root:
            return

        if not root.left and not root.right:
            height += 1
            res.append(height)
            return

        self.depth(root.left, height + 1, res)
        self.depth(root.right, height + 1,  res)


'''
思路：BFS
方法：
    scan every node by BFS
        save [node, height] in queue
        when meeting leaf, save height in res 
time complex: 
space complex: 
易错点：
'''
from collections import deque
class Solution:
    def allDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        queue = deque()
        queue.append([root, 1])

        res = []
        while queue:
            node, height = queue.popleft()
            if not node.left and not node.right:  # root is leaf
                res.append(height)
            if node.left:  # 必须有，否则node.left为None时，下个循环中，node为None，判断Node.left报错
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])
        return res
