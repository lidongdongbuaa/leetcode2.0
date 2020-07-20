#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 22:36
# @Author  : LI Dongdong
# @FileName: 106. Construct Binary Tree from Inorder and Postorder Traversal.py
''''''
'''
题目分析
1.要求：Given inorder and postorder traversal of a tree, construct the binary tree.
    
    Note:
    You may assume that duplicates do not exist in the tree.
    
    For example, given
    
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:
    
        3
       / \
      9  20
        /  \
       15   7
2.理解：create the tree by inorder and postorder list
3.类型：construct tree
4.确认输入输出及边界条件：
    input: two list, no repeated, node value range? N node number? N
    output:root of tree
    corner case: list is None : None
5.方法及方法分析：DFS + find mid, optimize find index of node
time complexity order: optimize find index of node O(N) < DFS + find mid O(N**2)
space complexity order: optimize find index of node O(N) = DFS + find mid O(N)
6.如何考
'''
'''
A. DFS + index
    Method
        post- order dfs(in_list, post_list), return root time O(N)
            end: post is None
            root = last elem of post_list's treeNode
            mid = in_list.index(last elem of postlist)  time complexity O(N)
            root.left = dfs(in_list left, post_list left)
            root.right = dfs(inlist right, post list right)
        time O(N**2) space O(N)
易错点：self.buildTree(inorder[:mid]... 是到mid，不能为mid
    postorder[mid : -1] 是到-2处，不能为-1
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:  # corner case
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid : -1])
        return root

'''
跟前一个方法比，内存消耗较少
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) != len(postorder):
            return None
        if len(inorder) == 0:
            return None

        def dfs(in_l, in_r, post_l, post_r):
            if in_l > in_r:
                return None

            root = TreeNode(postorder[post_r])
            index = inorder.index(postorder[post_r])

            root.left = dfs(in_l, index - 1, post_l, index - 1 - in_l + post_l)
            root.right = dfs(index + 1, in_r, index + 1 - in_r + post_r - 1, post_r - 1)

            return root

        return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)

'''
B. scale index size and use dict to save in_list
    Method
        1. transfer in_list to dict{value, index}
        2. def post-order recursion(in_l, in_r, post_l, post_r), return root
            end: in_l = in_r
            root = treenode(postlist [post_r - 1])
            mid = dict[postlist [post_r - 1]]
            root.left = recursion(in_l, mid, post_l, mid - in_l + post_l )
            root.right = recursion(mid + 1, in_r, post_r - 1 - in_r + mid + 1,post_r - 1)
        return root
    time O(N) space O(N)
易错点：treenode(postlist [post_r - 1])，dict[postlist [post_r - 1]], 是-1，不是在长度post_r处
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        dic = {value: index for index, value in enumerate(inorder)}

        def dfs(in_l, in_r, post_l, post_r):
            if in_l > in_r:
                return None

            root = TreeNode(postorder[post_r])
            mid = dic[postorder[post_r]]

            # 更新中序遍历、后序遍历边界，然后递归构建左右子树
            # 我们可以通过“中序和后序个数是相同”这个隐含条件，求出后序左右边界
            root.left = dfs(in_l, mid - 1, post_l, mid - 1 - in_l + post_l)
            root.right = dfs(mid + 1, in_r, mid + 1 - in_r + post_r - 1, post_r - 1)

            return root

        return dfs(0, len(inorder) - 1, 0, len(inorder) - 1)