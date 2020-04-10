#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 12:10
# @Author  : LI Dongdong
# @FileName: 337. House Robber III.py
''''''
'''
题目概述：树里的选择rob
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
在树中抢劫，不能相邻抢劫

input: root of tree; tree node number range is from 0 to 1000; node value is positive; order? No
output: amount number, int;
corner case: 
    root is None, return 0
    root is leaf, return its val

A. DP - dp(node), reach to node, the max amount; scan every node of this tree
    Method:
        1. corner case
        2. bottom - up idea, dp(node) = max(dp(node.left), dp(node.right), node.val + dp(node.left.child), node.val + dp(node.right.child))
        3. node is none, return 0
易错点：
    情况的分类
        1. 不抢本层root，故amount = 抢root.left + 抢root.right
        2. 抢本层root，故amount = root.val + root.left.child + root.right.child

Time complexity: O(N), N is node number
Space: O(H), H is height of the tree, average is log(N)
'''


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return root.val

        memo = {}

        def dp(node):  # return max amount when visit node
            # if not node.left and not node.right:
            #     return node.val
            if node in memo:
                return memo[node]

            if not node:  # end
                return 0

            not_do = dp(node.left) + dp(node.right)  # not rob root level
            ll = lr = rl = rr = 0  # rob root level
            if node.left:
                ll = dp(node.left.left)
                lr = dp(node.left.right)
            if node.right:
                rl = dp(node.right.left)
                rr = dp(node.right.right)
            res = max(not_do, node.val + ll + lr + rl + rr)
            memo[node] = res
            return res

        return dp(root)


'''
B. DP - dp(node) = a, b, a is amount while not robbing the node, b is amount while robbing the node
    Method:
        1. corner case
        2. dp(node) = dp(node.left)[1] + dp(node.right)[1], 

Time complexity: O(N), N is node number
Space: O(H), H is height of the tree, average is log(N)
'''


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return root.val

        memo = {}

        def dp(root):  # return amount robbing root and amout not robbing root
            if root in memo:
                return memo[root]
            if not root:
                return [0, 0]

            left = dp(root.left)  # left conditions
            right = dp(root.right)  # right conditions
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            rob = root.val + left[0] + right[0]
            res = [not_rob, rob]
            memo[root] = res
            return res

        return max(dp(root)[0], dp(root)[1])
