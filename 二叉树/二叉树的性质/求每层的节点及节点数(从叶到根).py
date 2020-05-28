#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 9:22
# @Author  : LI Dongdong
# @FileName: 求从叶到根的每层节点及节点数.py
''''''
'''
题目概述：
    Given binary tree 
        3
       / \
      9  20
        /  \
       15   7
    return 
    [
      [9, 15,7],
      [20],
      [3]
    ]
题目考点：
优化核心：
易错点：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
dfs 返回值模式
leaf为起始点，root为终点
'''
class Tree:
    def findLevelNode(self, root):
        if not root:  # corner case
            return []

        if not root.left and not root.right:
            return [1]

        from collections import defaultdict
        dic = defaultdict(int)

        def dfs(root): # return level height, root的高度为最大值，leaf为最小值
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            level = max(l, r) + 1
            dic[level] += 1
            return level

        dfs(root)
        return [val for val in dic.values()]