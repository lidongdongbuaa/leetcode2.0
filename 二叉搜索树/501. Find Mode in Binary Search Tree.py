#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 14:15
# @Author  : LI Dongdong
# @FileName: 501. Find Mode in 二分搜索 Tree.py
''''''
'''
题目概述：在有重复数值的BST中，找到众数，众数可能是多个
题目考点：BST中序遍历的性质，即数是递增的；BST中序遍历的迭代方法；dict的使用；求多个众数的思路
解决方案：先转化为dict，再求众数；在中序遍历中，求多个众数
方法及方法分析：dict转化法；BST的中序遍历迭代判断法
time complexity order: O(N)
space complexity order: BST的中序遍历迭代判断法 O(1) <  dict转化法 O(N)
如何考
'''
'''
find most frequenely occured elements

input:
    tree root node; node numb range? [0, +inif]; node value repeated? Y; order? BST
output:
    list[mode1], if have more than 1 mode, return [mode1, mode2]
corner case:
    root is None: -> []
    root is only one -> [root.val]

A. brute force - transfer as dict and output the mode
    Method:
        1. corner case
        2. preorder to traversal the tree, save tree nodes and count times in dict
        3. traversal the dict and find the mode, return
    Time complexity: O(N + N) = O(N) N is number of nodes
    Space: O(N) used in dict


'''


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [root.val]

        def transfer(root, node):  # use dict to save all node val and return
            if not root:
                return {}

            if root.val not in node:
                node[root.val] = 1
            else:
                node[root.val] += 1

            transfer(root.left, node)
            transfer(root.right, node)

        def findMode(nodes):  # return the modes in nodes dict
            if not nodes:
                return []

            maxTime = 0
            res = []
            for key, value in nodes.items():
                if value < maxTime:
                    pass
                elif value == maxTime:
                    res.append(key)
                else:
                    res = [key]
                    maxTime = value
            return res

        node = {}
        transfer(root, node)
        res = findMode(node)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
input: BST root; root number range is from 0 to 1000; have repeated value; 
output: the node value with mode
corner case
    if all node appear only once, return all node? Y
    root is None, return []

A. inorder traversal and accumulate
    Method:
        1. corner case
        2. inorder iterative traversal the tree
            1-2-2
            compare cur node value with pre node value
                if same, accumlate current node times
                else, save current time as preTime, set cur times = 1
            if current node times > pre node time, clear res stack, add cur node
            elif, =, add cur node to stack
            elif <, pass
        3. return res
    Time complexity: O(N), N is number of tree nodes
    Space: O(1)
易错点：
    1. 先积累目前的次数，可更新前值；再拿目前的次数与max次数进行比较
'''
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:  # corn case
            return []

        stack = []
        maxTimes = curTimes = 0
        preVal = float('-inf')
        res = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()

            if preVal ==  cur.val:
                curTimes += 1
            elif preVal < cur.val:
                curTimes = 1
                preVal = cur.val

            if curTimes == maxTimes:
                res.append(cur.val)
            elif curTimes < maxTimes:
                pass
            else:
                res = [cur.val]
                maxTimes = curTimes


            if cur.right:
                root = cur.right
        return res


