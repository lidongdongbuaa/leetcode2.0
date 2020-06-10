#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 9:25
# @Author  : LI Dongdong
# @FileName: 979. Distribute Coins in Binary Tree.py
''''''
'''
题目概述：给定一个树，树的节点值是不同的硬币数，移动硬币，让每一节点的硬币数都为1，求硬币移动的次数
题目考点：dfs 从下到上
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: tree; node number range is from 0 to inf; value range is sum of node == node number? Y; no order; have repeating
output: int, movement
corner case:
    root is None, return 0

numb of move -> coins in node  =>  abs(l) + abs(r)，即左右子树可以给与或接受coin数的绝对值的和

dfs bottom to top, return coins which the root can offer to outside
'''
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        self.res = 0
        def dfs(root):  # return coins the root can offer to outside
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            self.res = self.res + abs(l) + abs(r)
            return root.val - 1 + l + r

        dfs(root)
        return self.res

