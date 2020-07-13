#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 9:22
# @Author  : LI Dongdong
# @FileName: 2. Add Two Numbers.py
''''''
'''
题目分析
1.要求：You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        (2 -> 4 -> 3) + (5 -> 6 -> 4) -> (7 -> 0 -> 8)
2.理解：两个链表，数字对应的两两相加，不含前导0，即链表结束，数也就结束了；两个链表都非空
    与369题类似，可以深化为怎么求两个整数 (3 -> 4 -> 2) + (4 -> 6 -> 5)的和，即先转置成本题这样，再转置回去
3.类型：链表节点求和
4.方法及方法分析：两两值相加迭代法 转化为数字法
time complexity order: 
space complexity order:  
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
input: digit is saved in linked list; length of list? >= 1; value range? No limit; repeated? Y; order? reverse
123 -> 3->2-1; leading zero? N
output: linkedlist

if having leadin zero?
if not reverse?

A. brute force - transfer linkedlist as integer and add and transfer
    Method:
        1. transfer linkedlist to interger
            2->4->3  ->  342
        2. add one int to another
        3. transfer the combination to linkedlist, and return
    
    Time complexity: O(m + n), m and n is length of two linked list
    Space: O(1) 


'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        int1 = int2 = 0
        int1 = self.transfer(l1)
        int2 = self.transfer(l2)

        total = int1 + int2

        return self.reverseTransfer(total)

    def transfer(self, node):  # transfer linkedlist to integer
        if not node:
            return 0

        integer = 0
        times = 1
        while node:
            integer += node.val * times
            times *= 10
            node = node.next
        return integer

    def reverseTransfer(self, numb):  # transfer numb to linkedlist
        dummy = curr = ListNode(-1)
        for s in str(numb)[::-1]:
            curr.next = ListNode(int(s))
            curr = curr.next

        return dummy.next

'''
B. linked list combination - use carry to show the tens of digit
    Method:
        1. traversal every val in linkedlist A and linkedlist B
            add A val and B val and carry as sum
            use single digit of sum to build newNode
            give tens digit sum to carry
    
    Time: O(max(m,n))
    Space: O(1)
易错点:
    变量使用之前，一定要初始化 - 
    有一个算一个的迭代方法，分开使用if迭代
    求十分位是tens，个位是single digit
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(-1)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry = carry // 10
        return dummy.next



'''
test case
'''
b = ListNode(5)
a = ListNode(5)
x = Solution()
print(x.addTwoNumbers(a,b).val)