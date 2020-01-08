#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 9:58
# @Author  : LI Dongdong
# @FileName: 237. Delete Node in a Linked List.py
''''''
'''
237. Delete Node in a Linked List.py
题目分析
1.要求：Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.
2.理解：不给head，只给access to要删除的节点；删除除了尾节点之外的节点；不返回；节点的值不重复；
3.类型：删除题
4.方法及方法分析：复制跳跃next法
time complexity order: 复制跳跃next法O(1)
space complexity order: 复制跳跃next法O(1)
'''

'''
复制跳跃next法
思路：既然不知道要删除节点的前一个节点，即没法通过前节点跳跃本节点来删除节点，
    那就从本删除节点下手，把后一个节点的值复制到本节点，再跳跃后节点即可
方法：复制下个节点到本节点，跳过后一个节点，到下下个节点
边界条件：无
time complex: O(1)
space complex: O(1)
易错点：及时看example，可能文字真没看懂
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
