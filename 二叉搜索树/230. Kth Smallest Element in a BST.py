#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 10:05
# @Author  : LI Dongdong
# @FileName: 230. Kth Smallest Element in a BST.py
''''''
'''
题目概述：在tree中，查找第k个小的元素
题目考点：中序遍历的性质；中序遍历的两种方法
解决方案：得到中序遍历list，找到[k-1]；迭代中序遍历，得到k次node，后返回
方法及方法分析：list转化法；迭代中序遍历返回法
time complexity order: 迭代中序遍历返回法 O(H + k) < list转换法 O(N)
space complexity order: 迭代中序遍历返回法 O(H + k) < list转换法 O(N)
如何考
Following up: 如果BST插入/删除，以及找kth很频繁，如何优化找kth的时间？
    答：插入/删除，时间复杂度是O(H),找kth是O(H + K), 故总共是O(2H + k)
    故建立一个index structure by double linked list，此时 插入/删除O(H)，查找是O(k)，总共是tO(H + k),sO(N) to keep linked list
'''
'''
find kth smallest element

input:
    tree root: node number range? [0, +inf]; value range? N; BST
    k: value range? [1,tree node number]
output:
    node value : int
corner case
    root is None -> None

A. brute force - inorder traversal as list, find the list[k-1]
    Method:
        1. corner case
        2. inorder traveral the tree, save node value in list by recursion  tO(N)
        3. return [k - 1] value of list tO(1)
    Time: O(N) N is number of tree nodes
    Space: O(H), H is height of the tree, average is O(logN)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:  # corner case
            return None

        def recursion(root):  # return list saving all node value inorder
            if not root:
                return []

            res = []
            res += recursion(root.left)
            res.append(root.val)
            res += recursion(root.right)
            return res

        treeList = recursion(root)
        return treeList[k - 1]
'''
B.recursion - count the root times in inorder traversal, meet k, return k value by iterative in-order traversal
    Method:
        1. corner case
        2. in-order traversal the tree by iteration
            count the pop's node time, when reached to k, return this node value
    Time: O(H + K), H is height of tree used by add all left node in stack, then do k times to find kth element
        in average, H is logN, N is number of nodes, in worst case H is N for skewed tree
    space: O(H + k), in worst case, O(N + k), average O(logN + k)
易错点：时间空间复杂度    
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:  # corner case
            return None

        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val

            if cur.right:
                root = cur.right



