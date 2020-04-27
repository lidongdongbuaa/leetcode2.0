#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 9:25
# @Author  : LI Dongdong
# @FileName: 979. Distribute Coins in Binary Tree.py
''''''
'''
题目概述：给定一个树，树的节点值是不同的硬币数，移动硬币，让每一节点的硬币数都为1，求硬币移动的次数
题目考点：求硬币移动的次数 <- 求树多的/欠的硬币数 + 累加计算root+左右子树的总移动次数（虽然root不计入总移动次数中）
解决方案：分治 + 累加计算移动次数 + self.res
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
类似110. Balanced Binary Tree.py 
核心思路：hepler函数返回这个tree的coin跟1比的差值，是绝对值
'''
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0

        def helper(root):  # return the number of coins offer or given
            if not root:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            self.res += abs(l) + abs(r)
            return l + r + root.val - 1

        helper(root)
        return self.res

