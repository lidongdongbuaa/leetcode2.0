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
corner case: 
    root is None, return True
核心思想：分治；helper，返回高度；判断左边和右边的高度是否差超过1
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.res = True
        def helper(root):  # return max height
            if not root:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            if abs(l - r) > 1:
                self.res = False
            return max(l, r) + 1

        helper(root)
        return self.res


