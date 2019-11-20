#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 8:49
# @Author  : LI Dongdong
# @FileName: 708. Insert into a Cyclic Sorted List.py
''''''
'''
题目分析
1.要求：Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. 
    The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.
2.理解：在环链表中插入一个node，若链表为空，返回插入的链表；若链表不为空，返回原reference
3.类型：链表插入
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
list save method
idea：save all node in list, add node and rebuild the linklist
edge case：head is None
method：
    record reference, save all node in list; node_list, ref #tO(N), sO(N)
    add node val to the list #tO(1)
    sort the list #tO(NlgN)
    rebuild linklist and reference, return reference; dummy, ref_node  #tO(N), sO(N)
time complex: O(NlgN)
space complex: O(N)
易错点：
'''

'''
test case
'''