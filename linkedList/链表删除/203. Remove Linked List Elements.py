#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 22:22
# @Author  : LI Dongdong
# @FileName: 203. Remove Linked List Elements.py
''''''
'''
203. Remove Linked List Elements.py
题目分析
1.要求：Remove all elements from a linked list of integers that have value val.
2.理解：删除指定值的node，类似83删除重复node题
3.类型：删除链表
4.方法及方法分析：
time complexity order: next跳跃法O(N) = list保存法O(N)
space complexity order: next跳跃法O(1) < list保存法O(N)
'''

'''
list保存法
思路：list保存，去掉指定值，再构建链表
方法：链表迭代保存到list，但是遇到指定值跳过，然后重新构建这个链表
边界条件：head为空/list为空
time complex: O(N)
space complex: O(N)
易错点：考虑到list为空的情况
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None

        node_list = []
        while head: #tO(N),sO(N)
            if head.val == val:
                pass
            else:
                node_list.append(head.val) #tO(1)
            head = head.next

        if node_list == []:
            return None

        new_head = curr = ListNode(0)
        for elem in node_list: #tO(N),sO(N)
            new_node = ListNode(elem)
            curr.next = new_node
            curr = curr.next
        return new_head.next

'''
next跳跃法
思路：遇到指定的值，就nextnext进行跳过，直到遇到新的值，head再next
方法：链表用while迭代，然后用while判断是否跳完指定的值
边界条件：head = None
time complex: O(N)
space complex: O(1)
易错点：由于指定值可能为头节点，故要建立虚拟头节点;
        第二个while终止条件有两个，一是到链表末尾，二是值不等于指定值
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None

        dummy = prev = ListNode(0)
        prev.next = head
        while prev:#tO(N),sO(1)
            while prev.next and prev.next.val == val:
                prev.next = prev.next.next
            prev = prev.next
        return dummy.next



