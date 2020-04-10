#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 19:58
# @Author  : LI Dongdong
# @FileName: 1372. Longest ZigZag Path in a Binary Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

        Choose any node in the binary tree and a direction (right or left).
        If the current direction is right then move to the right child of the current node otherwise move to the left child.
        Change the direction from right to left or right to left.
        Repeat the second and third step until you can't move in the tree.
        Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
        
        Return the longest ZigZag path contained in that tree.
        
         
        
        Example 1:
        
        
        
        Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
        Output: 3
        Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
        Example 2:
        
        
        
        Input: root = [1,1,1,null,1,null,null,1,1,null,1]
        Output: 4
        Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
        Example 3:
        
        Input: root = [1]
        Output: 0
         
        
        Constraints:
        
        Each tree has at most 50000 nodes..
        Each node's value is between [1, 100]
2.理解：求zigzag路径长度的最大和
3.类型：遍历
4.确认输入输出及边界条件：
    input: tree root, same value in node,  at most 50000 nodes, node value [1, 100].
    output: int
    corner case:
        None -> 0
        only one -> 0
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. dfs + save left and right height
Method:
    1. corner case
    2. dfs(root, l, r) recursion, save res in self.res
        End: if not root
        Process: self.res = max(self.max, l, r)
        Trigger: 
            if left, self.dfs(root.left, r + 1, 0)
            if right, self.dfs（root.right, 0, l + 1)
            
易错点： 
    想出dfs的功能是什么
        1. 问题：求最长zz路径是多少
        2. 针对第一个节点，如何解决这个问题？   
            a.到第一个节点为止，其path长应该由其parent left or right(都为0)确定，故到了第一个节点，res = max(res, l, r),而l，r是上级传递下来的，故需要传递到下层
        3. 针对别的下层的，怎么解决
            a.有左右两个节点，故要分开解决
            b.针对左节点，若存在，需要针对源节点到左节点+1，故要把parent节点r转递到左节点的左, 而该左节点无右parent节点，故self.dfs(root.left, r + 1, 0 )
            c.针对右节点同理
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.left:
            return 1

        self.res = 0
        self.dfs(root, 0, 0)
        return self.res

    def dfs(self, root, l, r):  # renew and save length in res
        if not root:
            return

        self.res = max(self.res, l, r)
        if root.left:
            self.dfs(root.left, r + 1, 0)
        if root.right:
            self.dfs(root.right, 0, l + 1)
        return

