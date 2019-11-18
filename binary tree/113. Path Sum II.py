#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 10:47
# @Author  : LI Dongdong
# @FileName: 113. Path Sum II.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
method
idea：
edge case：
method：
time complex: 
space complex: 
易错点：
'''

'init.变量 + 递归'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []
        self.node_list = []

    def preorder(self, root, target):
        if not root:
            return
        self.node_list.append(root.val)
        if root.left is None and root.right is None and sum(self.node_list) == target:
            self.result.append(list(self.node_list))
        self.preorder(root.left, target)
        self.preorder(root.right, target)
        self.node_list.pop()

    def pathSum(self, root: TreeNode, sum: int):
        self.preorder(root, sum)
        return self.result


'主函数 + 递归'
class Solution:
    def preorder(self, root, target, node_list, result):
        if not root:
            return
        node_list.append(root.val)
        if root.left is None and root.right is None and sum(node_list) == target:
            result.append(list(node_list))
        self.preorder(root.left, target, node_list, result)
        self.preorder(root.right, target, node_list, result)
        node_list.pop()

    def pathSum(self, root: TreeNode, sum: int) -> bool:
        node_list = []
        result = []
        self.preorder(root, sum, node_list, result)
        return result




'''
test case
'''