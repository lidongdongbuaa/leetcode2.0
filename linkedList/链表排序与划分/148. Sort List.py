#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 9:14
# @Author  : LI Dongdong
# @FileName: 148. Sort List.py
''''''
'''
题目分析
1.要求：Sort a linked list in O(n log n) time using constant space complexity.
    Input: 4->2->1->3 Output: 1->2->3->4
    Input: -1->5->3->4->0 Output: -1->0->3->4->5
2.理解：用堆/快速/归并 三种nlongn的排序方法在原链表上进行排序，使得space complexity 为constant，即为常数
3.类型：链表排序
4.方法及方法分析： list storage-rebuild; method O(1) storage method
time complexity order:  O(1) storage method O(N) < list storage-rebuild method O(NlogN) 
space complexity order: O(1) storage method O(1) < list storage-rebuild method O(N) 
'''
'''
O(1) storage method
idea：
edge case：
method：
time complex: O(N)
space complex: O(1)
易错点：
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def go(self, head, k):
        cur = head
        for _ in range(k - 1):
            if cur.next is None:
                break
            cur = cur.next
        ret = cur.next
        cur.next = None
        return ret

    def merge(self, l1, l2):
        cur = buf = ListNode(0)
        while l1 or l2:
            if (l1 and l2 and l1.val < l2.val) or l2 is None:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return buf.next, cur

    def sortList(self, head):
        buf = ListNode(0)
        buf.next = head
        k = 1
        while True:
            lastHead = buf
            l1 = l2 = buf.next
            while l1:
                l2 = self.go(l1, k)
                if not l2:
                    break
                tail = self.go(l2, k)
                lastHead.next, lastHead = self.merge(l1, l2)
                l1 = tail
            lastHead.next =l1
            if l1 == buf.next and l2 is None:
                break
            k *= 2
        return buf.next

'''
不符合题意
list storage-rebuild method
idea：save node val in list -> sort list -> rebuild node/change val of linkedlist
edge case：head is None
method：
    traverse linkedlist to save node val in node_list #tO(N), sO(N)
    sort list #tO(NlogN)
    traverse node_list to rebuild the linkedlist #tO(N), sO(N)/sO(1)
time complex: O(NlogN)
space complex: O(N)
易错点：pre = new_head = ListNode(0)之后，返回的是new_head.next
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # edge case
        if head is None:
            return None

        # save linklist in a list
        node_list =[]
        curr = head
        while curr:
            node_list.append(curr.val)
            curr = curr.next

        # sort list
        node_list.sort()

        # rebuild the linklist
        pre = new_head = ListNode(0)
        for elem in node_list:
            new_node = ListNode(elem)
            pre.next = new_node
            pre = pre.next
        return new_head.next


'''
test case
'''
