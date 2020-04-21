#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 7:01
# @Author  : LI Dongdong
# @FileName: 143. Reorder List.py
''''''
'''
题目分析
1.要求：Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
    You may not modify the values in the list's nodes, only nodes itself may be changed.
    Not return anything, modify head in-place instead
2.理解：把链表的后半部分转置，然后挨个插入前半部分中;使用特殊list存储法(若最后把head.next = pre.next.next, 不用返回，故list也行)
3.类型：复杂排序
4.方法及方法分析：reverse-TwoPointer Method， list store-rebuild method
time complexity order: reverse-TwoPointer Method O(N) = list store-rebuild method O(N)
space complexity order: reverse-TwoPointer Method O(1) < list store-rebuild method O(N)
'''
'''
reverse-TwoPointer Method
idea: 双指针-数组, one ->front half head, another -> last half head; 
    reverse last half, meanwhile front half head points to last half
edge case：head is None/head.next is None; even or odd node numb
method：
    slow and fast node move to find the last half head, last_hd;#tO(N)
    last node of front half head points to None, f_end; #tO(1)
    reverse last half Linkedlist; new_last_hd #tO(N)
    traverse front half node and change pointer to new_last_hd one node by one node #tO(N)
time complex:  O(N)
space complex: O(1)
易错点：insert部分，前后两部分都需要及时备份；链表奇数偶数个时的处理
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None
        if head.next is None:
            return head

        # find the mid of Linkedlist
        slow_p = fast_p = head
        while fast_p and fast_p.next:
            front_end = slow_p
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        if fast_p is None:  # even
            last_hd = slow_p
            front_end.next = None
        elif fast_p.next is None:  # odd
            last_hd = slow_p.next
            slow_p.next = None

        # reversed last half Linked list
        new_last_hd = None
        while last_hd:
            next_hd = last_hd.next
            last_hd.next = new_last_hd
            new_last_hd = last_hd
            last_hd = next_hd

        # insert the reversed last half node to front half node
        while new_last_hd:
            next_hd = head.next
            next_last_hd = new_last_hd.next
            head.next = new_last_hd
            new_last_hd.next = next_hd
            head = next_hd
            new_last_hd = next_last_hd


'''
list store-rebuild method
思路：storage node val in a list, then change the oder in list;last rebuild the Linkedlist
边界条件：head is None/head.next is None
方法：
    traverse Linkedlist, store node val in node_list #sO(N) tO(N)
    traverse node_list, extract head and end val at same time, then store them in a new_list #sO(N) tO(N)
    traverse new_list to rebuild the new linkedlist; #sO(N) tO(N)
time complex: O(N)
space complex: O(N)
易错点：head.next = pre.next.next 由于不要求返回值，故必须在原有head上做改动，而直接赋值 head = new_head 不起作用，只有用next连接才行
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None
        if head.next is None:
            return head

        node_list = []
        curr = head
        while curr:  # transfer linklist val into list
            node_list.append(curr.val)
            curr = curr.next

        new_list = []
        length = len(node_list)
        for i in range(length // 2):  # rearrange order of value
            new_list.append(node_list[i])
            new_list.append(node_list[-(i + 1)])
        if length % 2 != 0:  # node numb of linklist is odd
            new_list.append(node_list[length // 2])

        new_head = pre = ListNode(0)
        for elem in new_list:
            new_node = ListNode(elem)
            new_head.next = new_node
            new_head = new_head.next

        head.next = pre.next.next


'''
test case
'''
