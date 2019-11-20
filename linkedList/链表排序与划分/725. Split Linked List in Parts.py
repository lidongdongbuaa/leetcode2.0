#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 20:53
# @Author  : LI Dongdong
# @FileName: 725. Split Linked List in Parts.py
''''''
'''
题目分析
1.要求：Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
2.理解：对链表(数组)进行k组分割，组之间数量差不能超过1，组可以为空，输出链表头
3.类型：链表分割
4.方法及方法分析： mathematical method
time complexity order: mathematical method O(N)
space complexity order: mathematical method O(N)
'''

'''
mathematical method
idea：find math logic in group number and numbers in group, then split linklist
edge case： head is None; length<k; length > k and length = k*n; length > k and length != k*n
method：
    traverse linklist to calculate length N of linklist # tO(N) sO(1)
    if length <= k, traverse linklist, split it, output every node and add none node # tO(N) sO(k)
    if length > k # tO(N) sO(k)
        if length = k*n, split linklist in k group and output
        if length != k*n,A group has N//k + 1 node, numb of A is N - N//k * k, B group has N//k node, numb of B is k - (N - N//k * k)
            split linklist and output
time complex: O(N)
space complex:  O(k)
易错点：链表一定要先保存head，再操作/ 情况的划分
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def buildGroup(self, head, contain, result):  # split contain numb node in linklist and save it in result
        temp = head
        for _ in range(contain-1):
            head = head.next
        next_head = head.next # backup next head
        head.next = None
        result.append(temp)  # add slipt node
        head = next_head
        return head, result

    def splitListToParts(self, root: ListNode, k: int):
        if root is None:  # edge case
            return k*[None]

        curr = root
        length = 0
        while curr:  # calcu length of linklist
            length += 1
            curr = curr.next

        if length <= k:  # length of linklist < k
            result = []
            while root:  # add every node to result
                temp = root
                next_hd = root.next  # backup next head
                temp.next = None
                result.append(temp)
                root = next_hd
            for _ in range(k - length):  # if length < k， add None
                result.append(None)
            return result
        elif length > k:
            if length % k == 0:
                result = []
                while root:  # split linklist into length//k smaller linklist
                    root, result = self.buildGroup(root, length // k, result)
                return result
            else:
                result = []   # split linklist into a/b two type group
                a_contain = length // k + 1  # elem a group contains
                b_contain = length // k  # elem b group contains
                a_numb = length - length // k * k  # numb of a
                b_numb = k - a_numb  # numb of b
                for _ in range(a_numb):  # begin to split linklist based on a/b
                    root, result = self.buildGroup(root, a_contain, result)
                for _ in range(b_numb):
                    root, result = self.buildGroup(root, b_contain, result)
                return result




'''
test case
'''

A1 = ListNode(1)
A2 = ListNode(2)
A3 = ListNode(3)
A4 = ListNode(4)
A5 = ListNode(5)
A6 = ListNode(6)



A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5
A5.next = A6

X = Solution()
print(X.splitListToParts(None,7))