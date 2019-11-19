#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 7:31
# @Author  : LI Dongdong
# @FileName: 147. Insertion Sort List.py
''''''
'''
题目分析
1.要求：Sort a linked list using insertion sort.
    Algorithm of Insertion Sort:
        Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
        At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
        It repeats until no input elements remain.
2.理解：利用插入比较法对链表进行排序
3.类型：链表排序
4.方法及方法分析：compare front node method
time complexity order: compare front node method O(N2)
space complexity order: compare front node method O(1)
'''

'''
compare front node method
idea：from first node beginning, compare it with next node, it > next, move next node 
edge case：head is None/ node val is negative/0/positive  
method：
    traverse node #t worst O(N2), best O(N) -> tO(N2); sO(1)
        if find curr node < next node:
            continue traverse
        elif curr node > next node, move next node:
            make curr pointer to the next next node
            find next node position by comparing it with all front node
                     
time complex: O(N2)
space complex: O(1)
易错点： pre = dummy  # reset pre
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:  # edge case
            return None

        dummy = pre = ListNode(0)  # build dummy head
        dummy.next = head

        while head and head.next:  # traverse linklist
            if head.val < head.next.val:  # if head and head next order is right
                head = head.next
            else:  # if order is wrong, find next node's right position
                next_hd = head.next  # reserve head next and next next node
                next_next_hd = head.next.next
                head.next = next_next_hd  # head pointer to next next node
                while next_hd.val > pre.next.val:  # find next_hd position, between pre and pre.next
                    pre = pre.next
                next_pre = pre.next  # reserve pre next node
                pre.next = next_hd  # change pointer
                next_hd.next = next_pre
                pre = dummy  # reset pre
        return dummy.next


'''
test case
'''