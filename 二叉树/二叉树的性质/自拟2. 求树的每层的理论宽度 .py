#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:06
# @Author  : LI Dongdong
# @FileName: 求每层的宽度.py
''''''
'''
题目分析
1.要求：求树的每层的理论宽度
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
bfs
dfs 自上而下
'''
class Tree:
    def findAllWidth(self, root):  # return list containing all width
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [1]

        from collections import deque
        queue = deque([(root, 1)])
        res = []

        while queue:
            res.append(queue[-1][1] - queue[0][1] + 1)
            n = len(queue)
            for _ in range(n):
                node, ind = queue.popleft()
                if node.left:
                    queue.append([node.left, ind * 2])
                if node.right:
                    queue.append([node.right, ind * 2 + 1])
        return res

class Tree:
    def findAllWidth(self, root):  # return list containing all width
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [1]

        dic = dict()

        def dfs(root, level, index):
            if not root:
                return

            if level not in dic:
                dic[level] = [index, index]
            else:
                dic[level][1] = index
            dfs(root.left, level + 1, index * 2)
            dfs(root.right, level + 1, index * 2 + 1)
            return

        dfs(root, 1, 1)
        res = [(end - start + 1) for (start, end) in dic.values()]
        return res


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return 1

        stack = [(root, 1, 1)]
        dic = {}

        while stack:
            root, level, index = stack.pop()
            if root:
                if level not in dic:
                    dic[level] = [index, index]
                dic[level][0] = index
                stack.append([root.right, level + 1, index * 2 + 1])
                stack.append([root.left, level + 1, index * 2])
        return [(end - start + 1) for (start, end) in dic.values()]