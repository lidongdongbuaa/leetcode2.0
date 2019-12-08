#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 9:14
# @Author  : LI Dongdong
# @FileName: 148. Sort List (linked list).py
''''''
'''
题目分析
1.要求：Sort a linked list in O(n log n) time using constant space complexity.
    Input: 4->2->1->3 Output: 1->2->3->4
    Input: -1->5->3->4->0 Output: -1->0->3->4->5
2.理解：用堆/快速/归并 三种nlongn的排序方法在原链表上进行排序，使得space complexity 为constant，即为常数
3.类型：链表排序
4.方法及方法分析： list storage-rebuild method； O(1) storage method
time complexity order:  O(1) storage method O(N) < list storage-rebuild method O(NlogN) 
space complexity order: O(1) storage method O(1) < list storage-rebuild method O(N) 
'''


'''
Merge sort method (iterative)
idea：use merge sort method
edge case：
    input:None? Y only one？ Y repeat？N value range? infinite
    output：None/linked list head
method：

time complex: O(NlogN)
space complex: O(N)
易错点：
'''




'''
Merge sort method (recursion)
idea：use merge sort method
edge case：
    input:None? Y only one？ Y repeat？N value range? infinite
    output：None/linked list head
method：
    divide the linked list into pairs 
    compare the node value of the pair, move the smaller val node left to the bigger one(by changing next to)
    compare elements of the two leftmost pairs, and move the smaller val node to the left. (by changing next to)
    repeat it until these is only one pair left

time complex: O(NlogN)
space complex: O(N)
易错点:L,R划定以后，尾部要及时中止，即L，R变成单独的
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:  # sort linklist
        if head is None:  # edge case
            return None
        if head.next is None:  # edge case
            return head

        length = self.len_linklist(head)
        mid = length // 2
        L = R = head  # L is head of first part, R is head of later part
        for _ in range(mid):
            R = R.next
        L_cur = L
        for _ in range(mid - 1):
            L_cur = L_cur.next
        L_cur.next = None

        sub_L = self.sortList(L)
        sub_R = self.sortList(R)

        return self.sortSubList(sub_L, sub_R)  # merge sub_L and sub_R

    def sortSubList(self, head1, head2):  # sort two sorted list
        if head1 is None:  # edge case
            return head2
        if head2 is None:
            return head1

        dummy = new_head = ListNode(0)
        while head1 and head2:  # merge two list
            if head1.val < head2.val:
                dummy.next = head1
                dummy = dummy.next
                head1 = head1.next
            else:
                dummy.next = head2
                dummy = dummy.next
                head2 = head2.next

        if head1:
            dummy.next = head1
        else:
            dummy.next = head2

        return new_head.next

    def len_linklist(self, head):  # calculate length of linked list
        if head is None:  # edge case
            return 0

        length = 0
        curr = head
        while curr:  # accumulate length
            length += 1
            curr = curr.next
        return length


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
            lastHead.next = l1
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
        node_list = []
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
