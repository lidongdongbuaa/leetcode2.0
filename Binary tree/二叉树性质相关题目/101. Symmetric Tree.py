#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:20
# @Author  : LI Dongdong
# @FileName: 101. Symmetric Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following [1,2,2,null,3,null,3] is not:
        1
       / \
      2   2
       \   \
       3    3
    Bonus points if you could solve it both recursively and iteratively.
2.理解： judge whether it is symmetric 
3.类型： binary features
4.确认输入输出及边界条件：
    input: root with definition, repeated? N order? N node numb range? N node value range? N
    output: True or false
    corner case: None? Y - False Only one? Y- True
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force - in-order scan
方法：
    1. in-order scan the tree, save node in list
    2. check the list
    
time complex: 
space complex: 
易错点：
'''