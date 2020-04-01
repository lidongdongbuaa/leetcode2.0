#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 9:34
# @Author  : LI Dongdong
# @FileName: 234. Palindrome Linked List.py
''''''
'''
题目分析
1.要求：Given a singly linked list, determine if it is a palindrome.
    Input: 1->2
    Output: false
2.理解：判断链表是否是回文
3.类型：判断链表结构
4.方法及方法分析：list储存判断法 reverse-TwoPointer Method
time complexity order: reverse-TwoPointer O(N) = Method list储存判断法 O(N)
space complexity order: reverse-TwoPointer O(1) < Method list储存判断法 O(N)
'''

'''
list储存判断法
思路：转换成list储存，然后通过比较头尾数值，遍历整个list进行判断
方法：
    traverse the linkedlist, save the node value in node_list #tO(N),sO(N)
    compare the node_list front and end value for all the value using iteration from 0 to mid index value #tO(N)
        if all front == end ->return True
        else: return False
边界条件：LinkedList = None/only one, return True/True
time complex: O(N)
space complex: O(N)
易错点：从头尾同时向中间迭代时，头部序号的起始是0，尾部的序号起始是-1不为-i，而是-(i+1)，故node_list[i] != node_list[-(i+1)]
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True #edge case

        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        for i in range(len(node_list)//2):
            if node_list[i] != node_list[-(i+1)]:
                return False
        return True


'''
reverse-TwoPointer Method
Idea：use two pointer in linkedlist so that in one traverse, we can scan the front and later part of linkedlist at the same time
Method：
    set slow pointer -> one node step, fast-p ->two step. traverse pointer, so when fast-p arrive at end, slow arrive at mid. 
        Meanwhile for slow-p, reverse its scaned node, set new_head. #tO(N/2) sO(1)
    traverse new_head and slow.next at the same time. compare new_head.val and slow.next.val, if they are equal, return True, else return false #tO(N/2) sO(1)
边界条件：LinkedList = None/only one, return True/True; length is odd or even 
time complex: O(N)
space complex: O(1)
易错点：链表迭代在写while的时候，一定要同时写next！！！不然会忘记！/ node 是even，slow-p要next；是odd，slow-p不用next
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        # edge case
        if head is None or head.next is None:
            return True

        slow_p = fast_p = head
        new_head = None
        while fast_p and fast_p.next:
            # fast pointer
            fast_p = fast_p.next.next
            # slow pointer and reverse it
            next_node = slow_p.next
            slow_p.next = new_head
            new_head = slow_p
            slow_p = next_node

        if fast_p is None:
            # compare front part with later part
            while new_head:
                if new_head.val != slow_p.val:
                    return False
                new_head = new_head.next
                slow_p = slow_p.next
            return True
        else:
            # slow pointer from mid to later part beginning
            slow_p = slow_p.next
            # compare front part with later part
            while new_head:
                if new_head.val != slow_p.val:
                    return False
                new_head = new_head.next
                slow_p = slow_p.next
            return True


'''
test case
'''
A1 = ListNode(0)
A2 = ListNode(0)
A3 = ListNode(3)
A1.next = A2


x = Solution()
x.isPalindrome(A1)