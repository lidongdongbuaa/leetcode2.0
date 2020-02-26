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
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. DFS + index
    Method:
        目的：
        post- order dfs(in_list, post_list), return root
            end: 
            root = last one of postlist
            mid = in_list.index(last one of postlist)
易错点：
'''