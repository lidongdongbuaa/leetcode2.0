# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 11:23
# @Author  : LI Dongdong
# @FileName: 21. Merge Two Sorted Lists.py
''
'''
题目分析
1.要求：Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two lists.
2.理解: 合并链表，只能用合并node的方式，不能用list重构法
3.类型：链表题，合并链表
4.方法：迭代法；递归法
time complexity order: 迭代法 O(m+n) = 递归法 O(m+n)
space complexity order: 迭代法 O(1) < 递归法 O(m+n)
'''
'''
Iterative法
思路：先边界，比较大小，然后用next连接
方法：建立新头，比较大小后，next连接
边界条件：l1 = None or l2 = None
time complex: O(m+n)
space complex: O(1)
'''
'''
merge two sorted linklist, result is sorted linklist

input:
    root: None?Y repeated? Y order? Y
output:
    head root
corner case:
    only is None: return other one
    both is None: return None

A.brute force - save val in list, merger, sorted, transfer as Linkist
    Time: O(max(m, n)) save in list + O(m / n) + O((m+n)log(m + n)) + O(m + n) = O((m+n)log(m+n))
    Space: O(m + n)

B. iterative linklist and create new one
    Method:
        1. corner case
        2. set newHead, interative l1 and l2, add the smaller one as new next node
    Time: O(m + n)
    Space: O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:  # corner case
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None

        dummy = cur = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                    cur = cur.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                    cur = cur.next
            elif l1:
                cur.next = l1
                break
            else:
                cur.next = l2
                break
        return dummy.next

'''
c. 递归
思路
    1. 返回的是新链表的头，为新变量，除此之外，不需要其他的新变量，故不需要helper()函数
    2. End：l1 或 l2 为空，返回l2 或 l1的头
    3. Trigger：
         l1 value < l2 value时，l1.next = 其余部分的头
         再返回此时的头l1
         else 同样
    Time: O(m + n)
    Space:O(m + n)
'''


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2