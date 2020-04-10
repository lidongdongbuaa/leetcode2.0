#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 19:41
# @Author  : LI Dongdong
# @FileName: 99. Recover 二分搜索 Tree.py
''''''
'''
题目概述：一个BST中，有两个值发生了对调，去寻找这两个值，在树上修正其值，不返回任何东西
题目考点：BST的中序遍历的性质：为上升序列； BST的中序遍历迭代法和递归法；两个值发生对调的两种子情况，1是相邻，2是不相邻的情况
解决方案：找到改变的x,y值或node;对树的值或node的值进行修改
方法及方法分析：转换list找xy法；中序遍历直接找法
time complexity order: O(N)
space complexity order: 中序遍历直接找法 O(H) < 转换list找xy法 O(H)
如何考
'''
'''
input: tree node; node number range? [0, +inf]
output: None
corner case: 
    root is None -> return 


A.brute force -
    Method:
        1. corner case
        1. traversal the tree inorder and save val in list
        2. find the two swaped value in list 4  2 3 1
        3. traversal the tree again and change value
    Time: O(N + N + N) = O(N)
    Space: O(N)

'''

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return

        def transfer(root):  # transfer root of tree to list
            if not root:
                return []

            res = []
            res += transfer(root.left)
            res.append(root.val)
            res += transfer(root.right)
            return res

        def findSwap(arr):  # return the two value which is swaped
            x = y = float('-inf')
            for i in range(len(arr) - 1):
                if x == float('-inf') and arr[i] > arr[i + 1]:
                    x = arr[i]
                    y = arr[i + 1]
                elif x != float('-inf') and arr[i] > arr[i + 1]:
                    y = arr[i + 1]
            return x, y

        def change(root):  # exchange values of nodes with value x, y
            if not root:
                return

            if root.val == x:
                root.val = y
            elif root.val == y:
                root.val = x

            change(root.left)
            change(root.right)


        tree_list = transfer(root)
        x, y = findSwap(tree_list)
        change(root)

'''
B. inorder traversal check - record the swap node and change
    Method:
        1. corner case
        2. use stack to iteratively inorder traversal the tree
            case1: if the swaped node is neighbor, 1324, record first node 1  and second node 3, after traversal, change value of them
            case2: if the swaped node is not neighbor, 4231, firstly record first 4 and second node 4,2, then renew cur node as 1, then exchange first and secodn node val
    
    Time: O(N)
    Space: O(H), H is height of tree, average value is O(logN)

    易错点：
        1. 先进行first和second的赋值，在进行pre的保存
        2.及时break
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:  # corner case
            return None

        stack = []
        pre = TreeNode(float('-inf'))
        first = None
        second = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()
            if pre.val >= cur.val:
                if first is None:  # case 1
                    first = pre
                    second = cur
                else:  # case 2
                    second = cur
                    break

            pre = cur  # 更新pre

            if cur.right:
                root = cur.right

        first.val, second.val = second.val, first.val


'''
C.recursion method
Time: worst case O(N), best is O(1)
Space: O(H) H is height of  the tree, to keep the recursion stack
'''


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def recursion(root, x, y, pre):
            if not root:
                return x, y, pre
            x, y, pre = recursion(root.left, x, y, pre)
            if root.val < pre.val:
                if x == None:
                    x = pre
                    y = root
                else:
                    y = root
            pre = root
            x, y, pre = recursion(root.right, x, y, pre)
            return x, y, pre

        x = y = None
        pre = TreeNode(float('-inf'))

        x, y, pre = recursion(root, x, y, pre)
        x.val, y.val = y.val, x.val

'''
D.  morris traversal
    Method:
        1. for in-order traversal, build new point,  node left point to its predecessor node, node right point to its successor node 
    Time O(N)
    Space O(1)
'''







