#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 9:25
# @Author  : LI Dongdong
# @FileName: 979. Distribute Coins in Binary Tree.py
''''''
'''
题目分析
1.要求：Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

    In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)
    
    Return the number of moves required to make every node have exactly one coin.
    
     
    
    Example 1:
    
    
    
    Input: [3,0,0]
    Output: 2
    Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
    Example 2:
    
    
    
    Input: [0,3,0]
    Output: 3
    Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
    Example 3:
    
    
    
    Input: [1,0,2]
    Output: 2
    Example 4:
    
    
    
    Input: [1,0,0,null,3]
    Output: 4
     
    
    Note:
    
    1<= N <= 100
    0 <= node.val <= N
2.理解：每个节点都为1，移动多余1的节点的值到为0的节点身上，数移动的次数
3.类型：从下到上的分治算法
4.确认输入输出及边界条件：
    input: root, root.val range [0, n], root numb [1,100]
    output: int
    corner case: node is None? Node
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. 每一个树的全部step = 左子树排出或引进的值的数量的绝对值 + 右子树的
易错点：子递归的含义是 该子树已经完好，需要排出或引进的值的数量
    self.step += abs(l) + abs(r)
    不要忘记 + 
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.step = 0

    def distributeCoins(self, root: TreeNode) -> int:
        if not root.left and not root.right:  # corner case
            return 0

        self.helper(root)
        return self.step

    def helper(self, root):  # return steps
        if not root:  # end condition
            return 0

        l = self.helper(root.left)
        r = self.helper(root.right)
        self.step += abs(l) + abs(r)  # 构建好整个树需要的步骤
        return l + r + root.val - 1  # 一个树整体向外排放或者吸收的value数量

