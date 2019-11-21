#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 7:23
# @Author  : LI Dongdong
# @FileName: 25. Reverse Nodes in k-Group.py
''''''
'''
题目分析
1.要求：Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    k is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    or k = 3, you should return: 3->2->1->4->5
    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.
2.理解：链表分段逆序，段长为k，O(1)的space complexity->不能用递归，只能迭代，不能用list保存； 不能改变node的值，只能改变next
3.类型：链表复杂逆序
4.方法及方法分析：part-reversed and together method
time complexity order: part-reversed and together method O(N)
space complexity order: part-reversed and together method O(1)
'''

'''
part-reversed and together method
idea：reverse k-node separately, then combine them together
edge case：head is None/n*k = length/n*k <length
method：
    traverse linklist, find the before node, head, after node of the k node #tO(N) sO(1)
    reverse the k node for n times #tO(N) sO(1)
time complex: O(N)
space complex: O(1)
易错点：分块的概念，每次处理完，要提供新的接口给下个循环
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseGroup(self, before, curr, after, k):
        new_before = curr
        for i in range(k):
            next_hd = curr.next
            curr.next = after
            after = curr
            curr = next_hd
        before.next = after
        new_head = curr
        return new_before, new_head


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # edge case
        if head is None:
            return None

        pre = before = ListNode(0)
        # node before k node
        before.next = head
        while head: #tO(k)*N/k = O(N) sO(1)
            curr = head
            # find the node after k node
            for _ in range(k): #tO(k) sO(1)
                # edge case:left node <k
                if head is None:
                    return pre.next
                head = head.next
            after = head
            # reverse k-node, output new before, new head
            before, head = self.reverseGroup(before, curr, after, k) #tO(k) sO(1)
        return pre.next

'''
test case
'''
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

x = Solution()
x.reverseKGroup(a,2)