#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 8:07
# @Author  : LI Dongdong
# @FileName: 662. Maximum Width of Binary Tree.py
''''''
'''
题目概述：求最大理论宽度
题目考点：bfs / dfs自上而下 + 用序号标记node，序号差为宽度
优化核心：
易错点：当tree 为 skewed tree时，每一层都为1，故每层的第一个数也要计算res
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

'''


'''
input: tree node, node number range is from 0 to inf; 
output: int, the max width
corner case
    if root is None,return 0
    if only root, return 1

BFS + index tag
Steps:
    1. create a queue with (node, node index)
    2. calculate the gap between the first node's index with last node's index, renew the res with the gap
    3. use for loop to popleft the all node, if it have child node, push them into the queue
    4. return res
Time complexity: O(n), n is number of nodes
Space: O(n), average case; in worse case, O(1)

'''

'''
corner case: 
    if root is None, return 0

max width -> index gap in same level
bfs + index gap
dfs 从上至下
'''
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        from collections import deque
        queue = deque([(root, 1)])
        res = 0

        while queue:
            n = len(queue)
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            for _ in range(n):
                root, index = queue.popleft()
                if root.left:
                    queue.append([root.left, index * 2])
                if root.right:
                    queue.append([root.right, index * 2 + 1])
        return res


'''
corner case: 
    if root is None, return 0

max width -> index gap in same level
bfs + index gap
dfs 从上至下，dfs(level, index), dic save the left node, self.res renew the res
'''
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return 1

        dic = {}
        self.res = 0
        def dfs(root, level, ind):
            if not root:
                return

            if level not in dic:
                dic[level] = ind
            self.res = max(self.res, ind - dic[level] + 1)  # 当tree 为 skewed tree时，每一层都为1，故res的计算要从第一个数开始

            dfs(root.left, level + 1, ind * 2)
            dfs(root.right, level + 1, ind * 2 + 1)
            return

        dfs(root, 1, 1)
        return self.res
'''
           1 
         (1, 1)
         /   \
        3     2
      (2, 2)  (2, 3)
       / \     \
      5   3     9
(3, 4)   (3, 5) (3, 7)

dic = {1:1, 2:2, 3:6}
res = max(0, 2) = 2 = max(2, 2) = 2 = max(2, 7-4 + 1) = 4
'''

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return 1

        stack = [(root, 1, 1)]
        dic = {}
        res = 0

        while stack:
            root, level, index = stack.pop()
            if root:
                if level not in dic:
                    dic[level] = index
                res = max(res, index - dic[level] + 1)
                stack.append([root.right, level + 1, index * 2 + 1])
                stack.append([root.left, level + 1, index * 2])
        return res

