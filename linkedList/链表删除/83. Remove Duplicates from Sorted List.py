#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 22:35
# @Author  : LI Dongdong
# @FileName: 83. Remove Duplicates from Sorted List.py
''''''
'''
题目分析
1.要求：Given a sorted linked list, delete all duplicates such that each element appear only once.
2.理解：删除排序链表的重复的节点，保证每个节点只出现一次，保留本值
3.类型：删除题
4.方法及方法分析：list保存法；next跳跃法
time complexity order: next跳跃法O(N) < list保存法O(N2)
space complexity order: next跳跃法O(1) < list保存法O(N)
'''

'''
list保存法 --也可用于非排序链表
思路：利用list去保存链表的值，用in判断是否已经存在
方法：迭代链表，用in判断是否已经存在，若不存在list里，加入list，最后重新构造这个链表
边界条件：head == None
time complex: O(N2)
space complex: O(N)
易错点：不能利用set，因为set虽然是不重复的，但是是无序的，即add有序加入，但是是无序保存的，与题目要求冲突
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        node_list = []
        while head: #（tO(N) + tO(1)）*N = tO(N2) ,sO(1)*N = sO(N)
            if head.val not in node_list: #tO(N)
                node_list.append(head.val) #tO(1),sO(1)
            head = head.next #tO(1)

        prev = new_node = ListNode(0)
        for elem in node_list:#tO(N),sO(1)
            node = ListNode(elem) #tO(1),sO(1)
            new_node.next = node #tO(1)
            new_node = new_node.next #tO(1)

        return prev.next

'''
next跳跃法
思路：利用链表已经排序的特性，采用next跳跃的方法进行跳过重复节点
方法：迭代链表，两个while，一个用来迭代所有链表，另一个用来寻找寻找不相同的node
边界条件：head为空；只有一个；只有两个；只有两个，且两个重复
time complex: O(N)
space complex: O(1)
易错点：边界条件的一一满足；第二个while只需要next跳跃，不需要head = head.next
        第二个while终止条件有两个，一是到链表末尾，二是遇到不重复的node
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head

        curr = head
        while curr: #tO(N),sO(1)
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next #核心
            curr = curr.next
        return head
        #也可以写为if形式，但是这里面的while虽然看起来在挨个循环，但是实际上在if成立时，curr的值是不变的，没有循环
        # while curr: #tO(N),sO(1)
        #     if curr.next and curr.val == curr.next.val:
        #         curr.next = curr.next.next #核心
        #     else:
        #         curr = curr.next
        # return head



head=ListNode(-1)
b=ListNode(0)
c=ListNode(0)
d=ListNode(0)
e=ListNode(0)
f=ListNode(3)
g=ListNode(3)
head.next=b
b.next=c
c.next=d
d.next=e
e.next = f
f.next = g

x=Solution()
print(x.deleteDuplicates(head).val)