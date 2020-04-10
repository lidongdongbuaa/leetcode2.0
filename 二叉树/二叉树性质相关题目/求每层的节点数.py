#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 9:14
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
思路：BFS
方法：
    while + width = len(queue) + for _ in range(queue)
time complex: 
space complex: 
易错点：for之后进行popleft
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def levelNodeNumb(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        width = 0
        res = []
        queue = deque([root])

        while queue:
            width = len(queue)
            res.append(width)
            for _ in range(width):  # traversal all same level node
                node = queue.popleft()  # 易错点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

'''
思路：DFS
方法：
    while + for
time complex: 
space complex: 
易错点：用level标记层数，用dic记录
'''

class Solution:
    def levelNodeNumb(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        level = 0
        dic = {}

        self. width(root, level, dic)
        return dic

    def width(self, root, level,  dic):  # output: dic
        if not root:  # corner case
            return {}

        if level not in dic:
            dic[level] = 1
        else:
            dic[level] += 1

        self.width(root.left, level + 1, dic)
        self.width(root.right, level + 1, dic)

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
print(x.levelNodeNumb(root))