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
dfs 自下而上
set root of tree as treeNode(None), named it as root
create dfs to scan the tree (preorder)
    root = treeNode(preorder first elem)
    find elem index in inorder as ind
    root.left = do dfs on left subtree (preorder[1:ind + 1], inorder[:index])
    root.right = do dfs on right subtree (preorder[ind + 1:], inorder[index + 1:])
    return root
run dfs and return res of it

易错点：对preorder和inorder分段位置的切割
time complexity: O(n^2) index use O(n) time
space:  O(n) in worst case
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root


'''
优化inorder.index()操作
使用dict的索引来替代index， 同时dfs内用索引，而不是preorder和inorder
易错点：原pre和in产生的left tree part 和 right tree part不是重叠的，故在确定pre的右边界时，要通过“前序和中序的节点个数相同”这个隐含条件，求出前序的右边界, 即 pre_r - pre_l  = in_r - in_l , 故pre_r = pre_l + in_r - in_l
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        dic = {v : k for k, v in enumerate(inorder)}

        def dfs(pL, pR, iL, iR):  # return root of constructed tree
            if pL >= pR or iL >= iR:
                return None

            root = TreeNode(preorder[pL])
            index = dic[preorder[pL]]

            root.left = dfs(pL + 1, index - iL + (pL + 1), iL, index)  # 这些参数中，pL+1/iL/index是明确确定的，剩下一个preorder right需要计算得出的
            root.right = dfs(pR - iR + (index + 1), pR, index + 1, iR)
            return root

        return dfs(0, len(preorder), 0, len(inorder))
