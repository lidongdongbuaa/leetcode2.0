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
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A. pre-order traversal 
Method: 
    main() corner case,  + return help()
    help(root, sum, tmp) use pre-order traversal to scan every path node, save them in list
        if sum of list = sum, return True
    after traversal, pop the last node in list by backtracking
time complex: O(N)
space complex: O(N)
易错点：
'''
class Solution:
    def findSum(self, root, sum):  # output: T/F
        if not root:  # corner case
            return False

        tmp = []
        if self.dfs(root, sum, tmp):
            return True
        else:
            return False

    def dfs(self, root, x, tmp):  # output: T/F
        if not root:  # corner case
            return False

        tmp.append(root.val)
        if not root.left and not root.right:  # root is leaf
            if sum(tmp) == x:
                return True


        res = self.dfs(root.left, x, tmp)
        if res == True:
            return True
        res = self.dfs(root.right, x, tmp)
        if res == True:
            return True
        tmp.pop()
# 没做完
