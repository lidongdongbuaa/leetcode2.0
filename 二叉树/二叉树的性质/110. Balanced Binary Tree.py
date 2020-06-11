# -*- coding: utf-8 -*-
# @Time    : 2/11/2020 8:28 PM
# @Author  : LI Dongdong
# @FileName: 110. Balanced Binary Tree.py
''''''
'''
题目概述：判断树是否平衡
题目考点：判断树是否平衡 <- 求树的最深深度是多少 + 对root左右深度差进行判断
解决方案：分治 + 判断左右深度 + self.res
方法及方法分析：
time complexity order: 
space complexity order:
如何考
'''
'''
input: tree root; node number range is from 0 to inf; 
output: True or False
corner case: 
    if not root, return True
    if only one node, return True
    
core: judge left and right height
转化为求左右子树的最大高度，从下往上判别 -> 最好用返回值法，其余两种方法也行，但是麻烦

dfs 自下而上
'''
# dfs, return max height
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True

        self.res = True
        def dfs(root):  # return max height of the tree
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l - r) > 1:
                self.res = False
            return max(l, r) + 1

        dfs(root)
        return self.res


