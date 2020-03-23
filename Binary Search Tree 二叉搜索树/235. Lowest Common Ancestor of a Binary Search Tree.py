#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 19:13
# @Author  : LI Dongdong
# @FileName: 235. Lowest Common Ancestor of a Binary Search Tree.py
''''''
'''
题目概述：在BST中，求两个点的最近公共祖先
题目考点：BST的左子树<root<右子树的性质；分治的思想；二分法
解决方案：root是mid，pq跟mid比较，划分下一个比较的区间
方法及方法分析：递归；迭代
time complexity order: O(N)
space complexity order: 迭代O(1) < 递归O(N)
如何考
'''
'''
find the lowest common ancestor of two tree node in a binary search tree

input: 
    tree root: None? Y; only one? Y 
    two node: val range? [in tree node val]; same? N;
output:
    tree node
corner case:
    root is None -> None
    root is only one -> None

three cases
    1. all in right
    2. all in left
    3. one in left, one in right; one in left, one in root; one in right, one in root -> return root

A. recursion 
    Method:
        1. corner case, case1 or case 2, return root
        2. start traversing the tree from the root node
        3. if both q and p in right subtree, do search with right tree starting step 2
        4. if both q and p in left subtree, do search with left tree starting step 2
        5. if step 3 and 4 are not true, that means we found the node which is common to node p and q subtrees, and hence return this common node as LCA

    Time complexity: O(N) N is number of nodes, in worst case, visit all nodes
    Space: O(N) in worst case, tree height is N

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:  # corner case
            return None
        if not root.left and not root.right:
            return None

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


'''
B. iterative method - find case 3 and return root
    Method:
        1. corner case
        2. traversal root
            check root.val with p val and q val, then choose root left or root right as root
            when meet case 3, return root

    Time complexity: O(N)
    Space:O(1)

易错点：空间复杂度是O(1)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:  # corner case
            return None
        if not root.left and not root.right:
            return None

        cur = root
        while cur:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

