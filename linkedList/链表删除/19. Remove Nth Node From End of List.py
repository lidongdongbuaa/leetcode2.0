#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 10:35
# @Author  : LI Dongdong
# @FileName: 19. Remove Nth Node From End of List.py
''''''
'''
题目分析
1.要求：Given a linked list, remove the n-th node from the end of list and return its head.
    Follow up:Could you do this in one pass?
2.理解：删除倒数第n个节点
3.类型：删除题
4.方法及方法分析：next跳跃法；list重构法；one-pass(two pointer)法
time complexity order: next跳跃法 O(N) =list重构法 O(N) = one-pass(two pointer)法 O(N)
space complexity order: next跳跃法 O(1) = one-pass(two pointer)法 O(1) < list重构法 O(N) 
'''

'''
next跳跃法
思路：找到正向位置，从要删除节点的前一个跳到要删除的后一个
方法：递归求从node数length；求出正向序数length-n；递归到length-n-1，跳到length-n+1
边界条件：head = None；head.next = None, n = 1
time complex: O(N)
space complex: O(1)
易错点：删除的节点是正向第一个,故建立空节点做为头，从头开始做；与237的区别是，237设定node不能是尾节点
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        if head.next == None and n == 1:
            return None

        curr = head
        length = 0
        while curr: #tO(N)
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(0,length - n): #tO(N-n) sO(1)
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next

'''
list重构法
思路：保存到list，删除对应节点的值，重构这个list
方法：递归保存list，用list.pop删除对应节点的值，再构建新的列表
边界条件：head = None；head.next = None, n = 1
time complex: O(N)
space complex: O(N)
易错点：
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        if head.next == None and n == 1:
            return None

        curr = head
        node_list = []
        while curr:
            node_list.append(curr.val) #tO(1) * N, sO(1) * N
            curr = curr.next #tO(1) * N

        node_list.pop(-n) #tO(n)

        prev = new_head = ListNode(0)
        for elem in node_list: #tO(1) * N, sO(N)
            prev.next = ListNode(elem)
            prev = prev.next
        return new_head.next


'''
one-pass(two pointer)法
思路：用两个node，并保持距离为n，故当第一个node到达尾部时，第二个node在-n处，正好开始next跳跃
方法：建立两个node，first_node先后移n次，然后first和second同时后移，直到first到达链表底部，然后进行next跳跃
边界条件：head = None；head.next = None, n = 1；n = length
time complex: O(N)
space complex: O(1)
易错点：first_node第一次移动和第二次移动次数的关系和判别关系for i in range(n)；while first_node.next
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        if head.next == None and n == 1:
            return None

        dummy = ListNode(0)
        dummy.next = head
        first_node = second_node = dummy
        for i in range(n): #tO(n)
            first_node = first_node.next
        while first_node.next: #tO(N-n),sO(1)
            first_node = first_node.next
            second_node = second_node.next
        second_node.next = second_node.next.next
        return dummy.next


