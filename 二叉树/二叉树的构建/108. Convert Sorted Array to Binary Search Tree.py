#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 8:58
# @Author  : LI Dongdong
# @FileName: 108. Convert Sorted Array to 二分搜索 Tree.py
''''''
'''
题目分析
1.要求：Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
    
    Example:
    
    Given the sorted array: [-10,-3,0,5,9],
    
    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
    
          0
         / \
       -3   9
       /   /
     -10  5
2.理解：use a sort list to build the height balanced BST
3.类型：create tree
4.确认输入输出及边界条件：
    input: sort list, no repeated value, ordered, node range? N node number? N
    output: root of tree, treeNode has been defined
    corner case:
        list is None -> None
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. binary search for mid of list as root, scale the list
    Method:
        dfs(), return root
            end: list is None
            root = treenode(mid of list)
            root.left = dfs(left half of list)
            root.right = dfr(right half of list)
        return root
    tO(N) visit every one exactly once 
    sO(N) O(N) to keep the output, and O(logN) for the recursion stack
易错点：
    1. 题目给出的升序数组就是二叉搜索树的中序遍历
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:  # corner case
            return None
        if len(nums) == 1:  # corner case 有效的减少了递归的次数
            return TreeNode(nums[0])

        length = len(nums)
        if length % 2 == 0:
            root = TreeNode(nums[length // 2 - 1])
            root.left = self.sortedArrayToBST(nums[:length // 2 - 1])
            root.right = self.sortedArrayToBST(nums[length // 2:])
        else:
            root = TreeNode(nums[len(nums) // 2])
            root.left = self.sortedArrayToBST(nums[:length // 2])
            root.right = self.sortedArrayToBST(nums[length // 2 + 1:])
        return root

'''
test code
corner case: 
None: return None
[-10,-3,0,5,9]
'''
'''
B. optimized odd/even case, scale the index
易错点：由于左边树node数量可以大于或小于右边树，故
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:  # corner case
            return None
        if len(nums) == 1:  # corner case 有效的减少了递归的次数
            return TreeNode(nums[0])

        length = len(nums)
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBST(nums[:length // 2])
        root.right = self.sortedArrayToBST(nums[length // 2 + 1:])
        return root

'''
C.iterative method
易错点：
    TreeNode(nums[mid])不是TreeNode(mid)
    全部闭区间
    rMid = (r - mid) // 2 + mid + 1
'''

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:  # corner case
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        length = len(nums)
        mid = length // 2
        res = root = TreeNode(nums[mid])
        stack = []
        stack.append([root, 0, length - 1, mid])

        while stack:
            root, l, r, mid = stack.pop()
            if mid < r:
                rMid = (r - mid) // 2 + mid + 1
                root.right = R = TreeNode(nums[rMid])
                stack.append([R, mid + 1, r, rMid])
            if l < mid:
                lMid = (mid - l) // 2 + l
                root.left = L = TreeNode(nums[lMid])
                stack.append([L, l, mid - 1, lMid])

        return res