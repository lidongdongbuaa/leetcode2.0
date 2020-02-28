#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 19:08
# @Author  : LI Dongdong
# @FileName: 105. Construct Binary Tree from Preorder and Inorder Traversal.py
''''''
'''
题目分析
1.要求：Given preorder and inorder traversal of a tree, construct the binary tree.
    
    Note:
    You may assume that duplicates do not exist in the tree.
    
    For example, given
    
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Return the following binary tree:
    
        3
       / \
      9  20
        /  \
       15   7
2.理解：前序中序构造二叉树
3.类型：二叉树的构造
4.确认输入输出及边界条件：
    input: two list with pre and in order tree node value, repeated? N, order? Y, node value range? N node number ? N
    output: root node of tree
    corner case: two list is None： None； Only one elem in two list: return treeNode
5.方法及方法分析：DFS + find mid, optimize find index of node
time complexity order: optimize find index of node O(N) < DFS + find mid O(N**2)
space complexity order: optimize find index of node O(N) = DFS + find mid O(N)
6.如何考
'''
'''
A. DFS + find mid
    Method：
        1. dfs(pre-list, in-list), return Tree node tO(N) sO(logN)
            end: prelist = None return None
            root = pre-list[0]
            index-in-ordr of pre-list[0] tO(N)
            root.left = dfs(left tree pre order, left tree right order)
            root.right = dfs(right tree pre order, left tree right order)
        time complexity: O(N**2) Space: O(N) since we store the entire tree.
易错点：本题假设node.val无重复
    in_index = inorder.index(preorder[0]),不是in_index = inorder.index(root)
    preorder的第一个在inorder的left和right的中间，在inorder的index也对应在preorder里，故可以把preorder分

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:  # corner case
            return None

        root = TreeNode(preorder[0])
        in_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: in_index + 1], inorder[:in_index])
        root.right = self.buildTree(preorder[in_index + 1:], inorder[in_index + 1:])
        return root


'''
B. optimize find index of node
    Method:
        1. transfer in-order list to dict{value: index}
        2. scale the index of preorder and inorder instead of scale themself during recursion
    time complexity O(N) space O(N)
易错点：
    if变为 pre_l == pre_r
    dic的简单创建
    对index的缩放
    原pre和in产生的left tree part 和 right tree part不是重叠的，故在确定pre的右边界时，要通过“前序和中序个数是相同”这个隐含条件，求出前序的右边界, 即 pre_r - pre_l  = in_r - in_l , 故pre_r = pre_l + in_r - in_l
'''


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:  # corner case
            return None
        dic = {value : i for i, value in enumerate(inorder)}
        return self.dfs(preorder, inorder, dic, 0, len(preorder), 0, len(inorder))

    def dfs(self, preorder, inorder, dic, pre_l, pre_r, in_l, in_r):  # return root
        if pre_l == pre_r:
            return None

        root = TreeNode(preorder[pre_l])  # 构建当前“根”
        index = dic[preorder[pre_l]]  # 从哈希表中找到当前“根”的索引

        # 更新前序遍历、中序遍历边界，然后递归构建左右子树
        # 我们可以通过“前序和中序个数是相同”这个隐含条件，求出前序的右边界
        root.left = self.dfs(preorder, inorder, dic, pre_l + 1, pre_l + 1 + index - in_l, in_l, index )
        root.right = self.dfs(preorder, inorder, dic, pre_l + 1 + index - in_l, pre_r, index + 1, in_r )
        return root

x = Solution()
x.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])


'''
preorder左右边界整理版
'''


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:

        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l == pre_r:
                return None

            root = TreeNode(preorder[pre_l])
            mid = dic[preorder[pre_l]]

            root.left = dfs(pre_l + 1, mid - in_l + pre_l + 1, in_l, mid)
            # root.right = dfs(mid - in_l + pre_l + 1, pre_r, mid + 1, in_r)
            root.right = dfs(pre_r - (in_r - (mid + 1)), pre_r, mid + 1, in_r)
            return root

        dic = {value : i for i, value in enumerate(inorder)}
        root = dfs(0, len(preorder), 0, len(inorder))
        return root
