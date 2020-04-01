#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 9:47
# @Author  : LI Dongdong
# @FileName: 369. Plus One Linked List.py
''''''
'''
题目分析
1.要求：Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
        You may assume the integer do not contain any leading zero, except the number 0 itself. [1,2,3] -> [1,2,4]
        The digits are stored such that the most significant digit is at the head of the list.
        Example :Input: [1,2,3] Output: [1,2,4]

2.理解：给了我们一个链表，用来模拟一个多位数，表头是高位，现在让我们进行加1运算 
3.类型：链表节点求和
4.方法及方法分析：转化为数字法,链表转置法
time complexity order:  链表转置法 O(N) = 转化为数字法 O(N) 
space complexity order: 链表转置法 O(1) < 转化为数字法 O(N)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
input: linkedlist head; None? N; length range? >= 1; value range? > 0; no leading zero? Y; order? most signficant digit is the head, 1->2->3 is 123
output:head of linklist


A.brute force - transfer as integer, add one, tranfer back
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        integer = 0
        cur = head
        while cur:
            integer = integer * 10 + cur.val
            cur = cur.next

        integer += 1

        dummy = curr = ListNode(-1)
        for i in str(integer):
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next

'''
B. reverse - reverse it, add one, reverse back
    Method:
        1. reverse 
            1->2->3 : 3 -> 2 -> 1
        2. add 1 to  last digit
            4->2-> 1
        3. reverse the it again
            1->2->4
    Time: O(N)
    Space O(N)

'''
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        curr = self.reverse(head)

        carry = 1
        dummy = newH = ListNode(-1)
        while curr or carry:
            if curr:
                carry += curr.val
                curr = curr.next
            newH.next = ListNode(carry % 10)
            newH = newH.next
            carry = carry // 10

        res = self.reverse(dummy.next)

        return res

    def reverse(self, head):  # return reversed linkedlist head
        curr = None
        while head:
            nextHead = head.next
            head.next = curr
            curr = head
            head = nextHead
        return curr




