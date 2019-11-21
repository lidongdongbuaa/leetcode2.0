#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 8:49
# @Author  : LI Dongdong
# @FileName: 708. Insert into a Cyclic Sorted List.py
''''''
'''
题目分析
1.要求：Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. 
    The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.
    Input: head = [3,4,1], insertVal = 2 Output: [3,4,1,2]
    Input: head = [], insertVal = 1 Output: [1]
    Input: head = [1], insertVal = 0 Output: [1,0]
2.理解：在环链表中插入一个node，若链表为空，返回插入后的链表；若链表不为空，返回原reference
3.类型：链表插入
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
list save method
idea：save all node in list, add node and rebuild the linklist
edge case：head is None / insertVal > < = 0? / 重复数值
method：
    record reference, save all node in list; node_list, ref #tO(N), sO(N)
    add node val to the list #tO(1)
    sort the list #tO(NlgN)
    rebuild linklist and reference, return reference; dummy, ref_node  #tO(N), sO(N)
time complex: O(NlgN)
space complex: O(N)
易错点：1.重复数值 [1,3,3] 在 if curr.val == ref.val:中的判断 -> 先加入第一个数，再循环判断
    2. 重复数值 [1,1,3] 在 if curr.val == ref.val:中的判断 -> 改为 if curr is ref:
有问题：leetcode ac 但是无法处理[1,3,1]，2的问题
'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:  # edge case, head is None
            head = Node(insertVal)
            head.next = head
            return head

        ref = curr = head
        node_list = []
        node_list.append(curr.val)  # save first node
        curr = curr.next
        while curr:  # save all node val in list
            if curr is ref:
                break
            node_list.append(curr.val)
            curr = curr.next

        node_list.append(insertVal)  # list add insertVal
        node_list.sort()  # sort list

        new_head = pre = Node(0)
        for elem in node_list:  # build new linklist
            new_node = Node(elem)
            pre.next = new_node
            pre = pre.next  # pre is end of linklist

        pre.next = new_head.next  # build circular linklist

        while pre.val != ref.val:  # find the reference
            pre = pre.next

        return pre

'''
test case
'''
A1 = Node(1)
A2 = Node(3)
A3 = Node(1)



A1.next = A2
A2.next = A3
A3.next = A1

X = Solution()
print(X.insert(A1, 2))