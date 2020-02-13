#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:06
# @Author  : LI Dongdong
# @FileName: 求每层的节点数.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：bfs + [node, index]
方法：
time complex: 
space complex: 
易错点：1. 修改deque为list
    2. 采用deepcopy(queue)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from copy import deepcopy
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        queue = []
        queue.append([root, 0])  # index from 0 to i in every level
        res = []

        while queue:
            length = len(queue)  # use length to control the scan range, not scan lower level node
            res.append(deepcopy(queue))
            for i in range(length):  # length 是实际宽度
                node, index = queue.pop(0)
                if node.left:
                    queue.append([node.left, 2 * index])
                if node.right:
                    queue.append([node.right, 2 * index + 1])
        return res
'''
思路：dfs + dic[level:index]
方法：
time complex: 
space complex: 
易错点：
'''
# 求tree的每层的节点数，求哪一层具有最多节点数，节点数是多少
# input: root
# output: dic：key：每层序数，value：每层的node个数
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        level = 0
        index = 0
        dic ={}  # store level and index
        self.res = []

        self.dfs(root, level, index, dic)
        print(dic)

    def dfs(self, root, level, index, dic):
        if not root:  # corner case
            return

        if level not in dic.keys():  # this level's first node show up firstly in dic, so store its level and index
            dic[level] = index
        else:
            dic[level] += index
        self.dfs(root.left, level + 1, index * 2, dic)
        self.dfs(root.right, level + 1, index * 2 + 1, dic)

from collections import deque
def constructTree(nodeList):  # input: list using bfs, output: root
    new_node = []
    for elem in nodeList:  # transfer list val to tree node
        if elem:
            new_node.append(TreeNode(elem))
        else:
            new_node.append(None)

    queue = deque()
    queue.append(new_node[0])

    resHead = queue[0]
    i = 1

    while i <= len(new_node) - 1:  # bfs method building
        head = queue.popleft()
        head.left = new_node[i]  # build left and push
        queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        queue.append(head.right)
        i = i + 2
    return resHead


root = constructTree([1,2,3,4,None,5])
x = Solution()
x.widthOfBinaryTree(root)