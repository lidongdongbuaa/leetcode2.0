#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 14:15
# @Author  : LI Dongdong
# @FileName: 501. Find Mode in Binary Search Tree.py
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


'''
B. inorder traversal the tree - count the time
    Method:
        1. corner case
        2. inorder traversal the tree by iteration method
            a. use ans list save [mode], record maxTimes, preNode, times
            b. renew the ans list
        3. return 
    Time: O(N) 
    Space: O(1)

易错点：
    1. 不要用复杂的变量命名，尤其是带s等，容易错，所以都不要带
    2. 修改代码时，要注意改完的代码和之前的变量命名是否一致
    3. 本题思路：先记录time，在比对max和time进行res值的替换
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [root.val]

        ans = []
        maxTimes = 0
        pre = TreeNode(float('-inf'))
        times = 0  # cur node appear times

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()

            if cur.val == pre.val:  # record times
                times += 1
            else:
                times = 1

            if maxTimes < times:
                ans = [cur.val]
                maxTimes = times
            elif maxTimes == times:
                ans.append(cur.val)
            else:
                pass

            pre = cur

            if cur.right:
                root = cur.right
        return ans
