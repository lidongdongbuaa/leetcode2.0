#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 8:13
# @Author  : LI Dongdong
# @FileName: 61. Rotate List.py
''''''
'''
题目分析
1.要求：Given a linked list, rotate the list to the right by k places, where k is non-negative.
    Input: 1->2->3->4->5->NULL, k = 2 / 0->1->2->NULL, k = 4
    Output: 4->5->1->2->3->NULL / 2->0->1->NULL
2.理解：把后k(k%N) 位节点挪到前面
3.类型：链表转置
4.方法及方法分析：list存储法(链表重建/列表更值)；next改变法
time complexity order: list存储法(链表重建/列表更值) O(N) = next改变法 O(N)
space complexity order: next改变法 O(1) < list存储法(链表重建/列表更值) O(N) 
'''

'''
list-store (rebuild) method
idea：store node val in list;proceed listl;use list to rebuild linklist
edge case：head is None/k > linklist length
method：
    traverse linklist, calcu length, store node val in list:length, curr, node_list; #tO(N), sO(N)
    calcu rest from k and length, proceed list and rebuild a new_list to store: rest,new_list; #tO(N), sO(N)
    traverse new_list to rebuild the linklist: pre = new_head #tO(N), sO(N)
time complex: O(N)
space complex: O(N)
易错点：两个list融合，是extend；大list套小list，是append
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # edge case
        if head is None:
            return None

        # calcu length/node list
        length = 0
        curr = head
        node_list = []
        while curr:
            length += 1
            node_list.append(curr.val)
            curr = curr.next

        # calcu rest
        rest = k % length

        # proceed list and rebuild a new list
        new_list = []
        new_list.extend(node_list[-rest:])
        new_list.extend(node_list[:-rest])

        #rebuild linklist
        pre = new_head = ListNode(0)
        for elem in new_list:
            new_node = ListNode(elem)
            pre.next = new_node
            pre = pre.next

        return new_head.next



'''
list-store (change node val) method
idea：store node val in list;proceed listl;use list to change linklist val
edge case：head is None/k > linklist length
method：
    traverse linklist, calcu length, store node val in list:length, curr, node_list; #tO(N), sO(N)
    calcu rest from k and length, proceed list and rebuild a new_list to store: rest,new_list; #tO(N), sO(N)
    traverse new_list to modify linklist val: curr = head  #tO(N), sO(1)
time complex: O(N)
space complex: O(N)
易错点：两个list融合，是extend；大list套小list，是append
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # edge case
        if head is None:
            return None

        # calcu length/node list
        length = 0
        curr = head
        node_list = []
        while curr:
            length += 1
            node_list.append(curr.val)
            curr = curr.next

        # calcu rest
        rest = k % length

        # proceed list and rebuild a new list
        new_list = []
        new_list.extend(node_list[-rest:])
        new_list.extend(node_list[:-rest])

        #modify original linklist val using newlist val
        pre = head
        for i in range(len(new_list)):
            pre.val = new_list[i]
            pre = pre.next

        return head

'''
change next method
idea：divide linklist into the rotated part and reserved part;change next to make rotated node ahead of reserved node
edge case：head is None/k > linklist length
method：
    traverse node to get length of linklist: curr,length #tO(N), sO(1)
    calcu rest of K to length:rest #tO(1), sO(1)
    based on rest，reserve reserved node head and tail, rotated node head and tail: res_hd, res_tail, rot-hd, rot_tail #tO(N), sO(1)
    reconnect these head and tail, return res_hd #tO(1)
time complex: O(N)
space complex: O(1)
易错点：res_tail后要归零！即res_tail.next = None; 涉及到head及head.next时，一定要考虑到其不存在的情况！！！
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # edge case
        if head is None:
            return None

        # calcu length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # calcu rest
        rest = k % length

        # case 1: rest = 0 (no change)
        if rest == 0:
            return head
        else:
            # case 2: rest != 0
            # reserved head/tail, rotated head/tail
            res_hd = head
            for _ in range(length - rest):
                res_tail = head
                head = head.next
                rot_hd = head

            while head:
                rot_tail = head
                head = head.next

            rot_tail.next = res_hd
            res_tail.next = None
            return rot_hd


'''
test case
'''