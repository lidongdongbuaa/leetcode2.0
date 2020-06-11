#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 7:15
# @Author  : LI Dongdong
# @FileName: 543. Diameter of Binary Tree.py
''''''
'''
题目概述：求两个子叶之间的最长路径
题目考点：dfs求路径+self.res
优化核心：无
易错点：l和r是左右子树的最大节点数，故计算res时，直接l+r求得路径长度
方法及方法分析：
time complexity order: O(N)
space complexity order: O(logN)
如何考
'''

'''
求子叶之间的最长路径 -> 求树的最深深度
dfs 自下而上
self.res = max(self.res, l + r)
'''


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0

        def pathLength(root):  # return max length
            if not root:
                return 0

            l = pathLength(root.left)
            r = pathLength(root.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1

        pathLength(root)
        return self.res