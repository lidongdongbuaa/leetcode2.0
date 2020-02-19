#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:06
# @Author  : LI Dongdong
# @FileName: 求每层的宽度.py
''''''
'''
题目分析
1.要求：求每层中，左边第一个到右边第一个的宽度
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
    deque record node and index (2* index (+1))
    traversal all nodes, calculate index dif of every level node by for loop
time complex: 
space complex: 
易错点：
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        width = 0
        res = []
        queue = deque()
        queue.append([root, 0])

        while queue:
            width = len(queue)
            left = queue[0][1]
            right = queue[-1][1]
            res.append(right - left + 1)
            for _ in range(width):  # traversal all same level node
                node, index = queue.popleft()  # 易错点
                if node.left:
                    queue.append([node.left, index * 2])
                if node.right:
                    queue.append([node.right, index * 2 + 1])
        return res
'''
思路：dfs + dic[level:index]
方法：
    main: set level, index, dic
    helper: 
        DFS scan every node, renew level and index  = index * 2 （+ 1）
        save dic[level] = [first node index, other node index]
time complex: 
space complex: 
易错点：dic[level] = max(index + 1, dic[level])
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
        self.res = 0

        self.dfs(root, level, index, dic)
        return dic

    def dfs(self, root, level, index, dic):
        if not root:  # corner case
            return

        if level in dic:
            dic[level][1] = index
        else:
            dic[level] = [index, index]

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


root = constructTree([1,2,3,None,5,6])
x = Solution()
x.widthOfBinaryTree(root)