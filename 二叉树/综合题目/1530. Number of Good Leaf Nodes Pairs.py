#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:54
# @Author  : LI Dongdong
# @FileName: 1530. Number of Good Leaf Nodes Pairs.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0

        def dfs(root):  # return 子树结点个数 as list
            if not root:
                return []
            if not root.left and not root.right:
                return [1]

            l = dfs(root.left)
            r = dfs(root.right)

            if root.left and root.right:
                self.res += calculatePos(l, r)

            ans = l + r
            return [elem + 1 for elem in ans]

        def calculatePos(l1, l2):
            ans = 0

            for x in l1:
                for y in l2:
                    if x + y <= distance:
                        ans += 1
            return ans

        dfs(root)
        return self.res
