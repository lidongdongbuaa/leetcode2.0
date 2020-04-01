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
4.方法及方法分析： Bottom-up Merge sort method； Merge sort method； list storage-rebuild method
time complexity order: Bottom-up Merge sort method O(NlogN) = Merge sort method O(NlogN) = list storage-rebuild method O(NlogN)
space complexity order:  Bottom-up Merge sort method O(1) < Merge sort method O(N) = list storage-rebuild method O(N)
'''

'''
Bottom-up Merge sort method (iterative)
idea：use bottom-up merge sort method
edge case：
    input:None? Y only one? Y repeat? N sorted? N range ? N
    output：None / the sorted linked list head
method：
    compare the value of the adjacent node groups having one element, by calculating linklist length, using while, for loop, moving head to cut the groups
    compare the value of the adjacent node groups have two elements
    Then repeat doing it, until there is only one group
time complex: O(NlogN)
space complex: O(1)
易错点： 在求第二段的头尾时，第二段的长度可能会小于gap的长度，故需要使用if head: s_end = head, head = head.next避免head.next报错
'''
'leetcode 超时。' \
'原因：interval for循环中，重复性寻找每段的头和尾' \
'解决方案：舍弃掉for循环，用while head和interval'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:  # sort linklist
        if not head:  # corner case
            return None
        if not head.next:
            return head

        length = self.findL(head)  # calculate length
        gap = 1
        cur = head
        dummy = ListNode(0)
        dummy.next = head

        while gap < length:  # do bottom-up merge
            for i in range(0, length - gap, gap * 2):
                dummy = self.merge(dummy, i, gap)
            gap = gap * 2
        return dummy.next

    def findL(self, head):  # calculate lenght
        if not head:  # corner case
            return 0

        numb = 0
        while head:  # accumlate length
            head = head.next
            numb += 1
        return numb

    def merge(self, dummy, i, gap):  # merge sort first gap nodes with second gap nodes
        head = dummy
        for _ in range(i + 1):
            b = head  # before-head of first gap nodes
            head = head.next
            f = head  # head of first gap nodes

        for _ in range(gap):
            f_end = head  # tail of first gap nodes
            head = head.next
            s = head  # head of second gap nodes

        for _ in range(gap):
            if head:  # 易错点
                s_end = head  # tail of second gap nodes
                head = head.next
            next = head  # head of next part(except sort nodes)

        b.next = None
        f_end.next = None
        s_end.next = None

        newH, newT = self.submerge(f, s)
        b.next = newH
        newT.next = next
        return dummy

    def submerge(self, fH, sH):  # merge two sorted linked list fH and sH, output head and tail
        if not sH:
            head = fH
            while head.next:
                head = head.next
            return fH, head

        if not fH:
            head = sH
            while head.next:
                head = head.next
            return sH, head

        dummy = cur = ListNode(0)
        while fH and sH:  # or 可以吗
            if fH.val < sH.val:
                cur.next = fH
                cur = cur.next
                fH = fH.next
            else:
                cur.next = sH
                cur = cur.next
                sH = sH.next

        if fH:
            cur.next = fH
        if sH:
            cur.next = sH

        while cur.next:
            cur = cur.next
        return dummy.next, cur


'optimized code'
'''
关键点：
    1. 用while head 替换 for
    2. 每轮 merge之前，每次更新fake_tail和head
    3. 每轮 merge中，先cut，后merge，再链接merged linklist，最后更新fake_tail和head
易错点：新group的head，tail，与前group，后group的连接
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:  # sort linklist
        if not head:  # corner case
            return None
        if not head.next:
            return head

        length = self.findL(head)  # calculate length
        interval = 1
        dummy = ListNode(0)
        dummy.next = head

        while interval < length:  # do bottom-up merge
            fake_tail = dummy  # fake_tail is tail of last part, 初始化
            head = dummy.next
            while head:
                nextH = self.cut(head, interval)
                leftH = self.cut(nextH, interval)
                mergeHead, mergeTail = self.merge(head, nextH)
                fake_tail.next = mergeHead  # connect the merged part to original linklist
                mergeTail.next = leftH
                fake_tail = mergeTail  # renew the tail which is before the merge sort part
                head = leftH  # renew the head
            interval = 2 * interval

        return dummy.next

    def findL(self, head):  # calculate lenght
        if not head:  # corner case
            return 0

        numb = 0
        while head:  # accumlate length
            head = head.next
            numb += 1
        return numb

    def cut(self, head, interval):  # from head to cut interval nodes, return next part head
        if not head:  # corner case
            return None

        for _ in range(interval):
            if not head:  # corner case: interval > length of linklist
                break
            tail = head
            head = head.next
        tail.next = None
        return head

    def merge(self, head1, head2):  # merge sort two sorted linklist. return this part head and tail
        if not head1:
            cur = head2
            while cur.next:
                cur = cur.next
            return head2, cur
        if not head2:
            cur = head1
            while cur.next:
                cur = cur.next
            return head1, cur

        dummy = cur = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next

        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        while cur.next:
            cur = cur.next
        return dummy.next, cur


A1 = ListNode(-1)
A2 = ListNode(5)
A3 = ListNode(3)
A4 = ListNode(4)
A5 = ListNode(0)
A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5

X = Solution()
X.sortList(A1)

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
        L = R = head  # L is head of first part,  R is head of later part
        for _ in range(mid):  # cut separated L group and R group
            R = R.next
        L_cur = L
        for _ in range(mid - 1):  # L_cur is first part's tail
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
list storage-rebuild method
idea：save node val in list -> sort list -> rebuild node/change val of linkedlist
edge case：head is None
method：
    traverse linkedlist to save node val in node_list #tO(N), sO(N)
    sort list #tO(NlogN)
    traverse node_list to rebuild the linkedlist #tO(N), sO(N)/sO(1)
time complex: O(NlogN)
space complex: O(N)
易错点：因为pre = new_head = ListNode(0)，故最后需要返回new_head.next，而不是new_head
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
