#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 8:49
# @Author  : LI Dongdong
# @FileName: 708. Insert into a Cyclic Sorted List.py
''
'''
题目分析
1.要求：Given a node from a cyclic linked list which is sorted in ascending order, 
    write a function to insert a value into the list such that it remains a cyclic sorted list. 
    The given node can be a reference to any single node in the list, 
    and may not be necessarily the smallest value in the cyclic list.
    Input: head = [3,4,1], insertVal = 2 Output: [3,4,1,2]
    Input: head = [], insertVal = 1 Output: [1]
    Input: head = [1], insertVal = 0 Output: [1,0]
2.理解：在环链表中插入一个node，若链表为空，返回插入后的链表；若链表不为空，返回原reference
3.类型：链表插入
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.自拟题：在sorted single linklist 插入node，keep linklist sorted
'''

'''
list save method
idea：save all node in list, add node and rebuild the linklist
edge case：head is None / insertVal > < = 0? / linklist has repeated val
method：
    record reference, save all node in list; node_list, ref #tO(N), sO(N)
    add node val to the list #tO(1)
    sort the list #tO(NlgN)
    rebuild linklist and reference, return reference; dummy, ref_node  #tO(N), sO(N)
time complex: O(NlgN)
space complex: O(N)
易错点：1.迭代圆环的终止判断：重复数值 [1,3,3] 在 if curr.val == ref.val:中的判断 -> 先加入第一个数，再循环判断
    2. 迭代圆环的终止判断：重复数值 [1,1,3] 在 if curr.val == ref.val:中的判断 -> 改为 if curr is ref:
有问题：leetcode accept 但是无法处理[1,3,1]，2的问题，即对于有头节点相同值的链表来说，1-1-2-3，本题默认head指向第一个1
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
        node_list = [curr.val]
        curr = curr.next
        while curr is not ref:  # save all node val in list
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
iteration method
idea：iterative linklist and find suitable position to insert the node
edge case：head is None/ head.next is None / insertVal > < = 0? / linklist has repeated val
method：
    head is None, add node
    save ref
    head is only one node -> insertVal>/< head.val -> merged by following case
    iterative to judge whether all node is repeated in linklist, #tO(N), sO(1)
        if yes, insert node -> merged by following case
        if No, iterative linklist 
            if insert node val = one node val, insert node (2-3-5 2 -> 2-2-3-5)
            if node next val < node val < insert node val, insert node (2-3-5 6 -> 2-3-5-6)
            if insert node val < node next val < node val , insert node (2-3-5 1 -> 2-3-5-1)
            if node val < insert node val < next node val, insert node (2-3-5 4 -> 2-3-4-5)
            if head is ref -> all node are same, insert node
time complex: O(N)
space complex: O(1)
易错点：处理链表中全是重复node的问题，例如[3,3,3];对linklist分类合理；function名用的时候不要搞混
'''
class Solution:
    def insertNode(self, head, insertVal):
        next_node = head.next
        new_node = Node(insertVal)
        head.next = new_node
        new_node.next = next_node

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:  # edge case, head is None
            head = Node(insertVal)
            head.next = head
            return head

        ref = head  # backup head
        head = head.next
        while ref is not head:  # judge whether linklist is full of repeated node
            if ref.val != head.val:
                repeat = 0  # linklist is not full of repeated node
                break
            head = head.next
        else:
            repeat = 1  # linklist is full of repeated node

        if repeat == 1:  # linklist is full of repeated node
            self.insertNode(head, insertVal)
            return head
        else:  # linklist is not full of repeated node
            ref = head
            while head:  # iterative node, four case of node
                if insertVal == head.val:
                    self.insertNode(head, insertVal)
                    return ref
                elif insertVal > head.val > head.next.val:
                    self.insertNode(head, insertVal)
                    return ref
                elif insertVal < head.next.val < head.val:
                    self.insertNode(head, insertVal)
                    return ref
                elif head.val < insertVal < head.next.val:
                    self.insertNode(head, insertVal)
                    return ref
                head = head.next

'Optimized code'
class Solution:
    def insertNode(self, head, insertVal):
        next_node = head.next
        new_node = Node(insertVal)
        head.next = new_node
        new_node.next = next_node

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:  # edge case, head is None
            head = Node(insertVal)
            head.next = head
            return head

        ref = head
        while head:  # iterative node, four case of node
            if insertVal == head.val:
                self.insertNode(head, insertVal)
                return ref
            elif insertVal > head.val > head.next.val:
                self.insertNode(head, insertVal)
                return ref
            elif insertVal < head.next.val < head.val:
                self.insertNode(head, insertVal)
                return ref
            elif head.val < insertVal < head.next.val:
                self.insertNode(head, insertVal)
                return ref
            head = head.next
            if head is ref:  # all node are same
                self.insertNode(head, insertVal)
                return head


'''
test case
'''
A1 = Node(3)
A2 = Node(3)
A3 = Node(3)

A1.next = A2
A2.next = A3
A3.next = A1

X = Solution()
print(X.insert(A1, 0))
