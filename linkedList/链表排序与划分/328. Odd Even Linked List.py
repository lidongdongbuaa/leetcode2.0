#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 9:13
# @Author  : LI Dongdong
# @FileName: 328. Odd Even Linked List.py
''''''
'''
题目分析
1.要求：Given a singly linked list, group all odd nodes together followed by the even nodes. 
    Please note here we are talking about the node number and not the value in the nodes.
    You should try to do it in place. 
    The program should run in O(1) space complexity and O(nodes) time complexity.
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on .
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL
2.理解：把合并后的奇数位的node放在合并后的偶数位的node之前，只能改变next，不能用list存储法
3.类型：链表转置
4.方法及方法分析：奇偶合并法
time complexity order: 奇偶合并法O(N)
space complexity order: 奇偶合并法O(1)
'''

'''
奇偶合并法
思路：head指向3/5/7;headnext指向2/4/6
方法：及时保存head.next;及时保存头节点；改变next指向
边界条件：head = None, head.next = None, head.next.next = None
time complex: O(N)
space complex: O(1)
易错点：while head.next and head.next.next 不是or
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head

        prev_head = head
        prev_next_head = head.next

        while head.next and head.next.next:
            next_head = head.next
            head.next = head.next.next
            next_head.next = next_head.next.next
            head = head.next
        head.next = prev_next_head
        return prev_head
