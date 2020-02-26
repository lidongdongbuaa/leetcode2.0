# -*- coding: utf-8 -*-
# @Time    : 2/11/2020 11:44 AM
# @Author  : LI Dongdong
# @FileName: 构造Binary Tree.py
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
A.
思路：bfs
方法：
time complex: 
space complex:
易错点：while i的判断
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        if head.left:
            queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        if head.right:
            queue.append(head.right)
        i = i + 2
    return resHead


root = constructTree([1,2,3,4,None,5])
