#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 9:57
# @Author  : LI Dongdong
# @FileName: 708. 自拟题.py
''''''
'''
自拟题1
1.要求：在sorted single linklist 插入node，keep linklist sorted
2.理解：在单链表中插入node
3.类型：链表插入
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    for linklist, it is None? it has only one node? has repeated Node? all node are repeated? 
        the node value range?
    for insertVal, it = linklist node val? value range?
'''

'''
list save method
idea： save all node val in list, add the insert node val, then sort the list. finally rebuild the linklist based on the list
method：
    head is None, build new one #tO(1)
    iterative linklist, save node val in list; node_list  #tO(N), s(N)
    add insertVal in list #tO(1), s(1)
    sort list #tO(NlgN), s(1)
    iterative list, rebuild the linklist; new_head #tO(N), s(N)
time complex: O(NlgN)
space complex: s(N)
易错点：
'''

'''
iterative linklist method
idea： iterative linklist, find the suitable place to insert the insertVal
method：
    Linklist is None, add node
    save ref
    Linklist has only one node -> insertVal>/< head.val. -> merged by following case
    Linklist has > one node
        iterative linklist :  # tO(N), sO(1)
            if insertVal < node val, insert, return 
            if insertVal = node val, insert, return
        node val > end node, insert, return
time complex: O(N)
space complex: O(1)
易错点：
'''
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertNode(self, head, insertVal):
        next_node = head.next
        new_node = Node(insertVal)
        head.next = new_node
        new_node.next = next_node

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:  # head is None
            head = Node(insertVal)
            return head

        pre = dummy = Node(0)
        pre.next = head
        while head:  # iterative linklist
            if insertVal < head.val:  # insertVal < one node
                self.insertNode(pre, insertVal)
                return dummy.next
            elif insertVal == head.val:  # insertVal = one node
                self.insertNode(pre, insertVal)
                return dummy.next
            pre = head  # find end node of linklist
            head = head.next

        new_node = Node(insertVal)  # insertVal > all node
        pre.next = new_node
        return dummy.next

        # if head.next is None:  # linklist has only one node
        #     if insertVal < head.val:
        #         new_node = Node(insertVal)
        #         new_node.next = head
        #         return new_node
        #     elif insertVal > head.val:
        #         new_node = Node(insertVal)
        #         head.next = new_node
        #         return head

'''
自拟题2
1.要求：在部分sorted single linklist 中插入node，keep linklist sorted
    即[4,5,1,2,3]中
2.理解：在部分sort单链表中插入node
3.类型：链表插入
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    for linklist, it is None? it has only one node? has repeated Node? all node are repeated? 
        the node value range?
    for insertVal, it = linklist node val? value range?
'''

'''
test case
'''
A1 = Node(1)
# A2 = Node(3)
# A3 = Node(5)
# A4 = Node(7)
#
# A1.next = A2
# A2.next = A3
# A3.next = A4

X = Solution()
print(X.insert(A1, 3))