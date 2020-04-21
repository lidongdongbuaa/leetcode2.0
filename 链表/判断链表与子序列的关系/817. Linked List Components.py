#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 7:42
# @Author  : LI Dongdong
# @FileName: 817. Linked List Components.py
''''''
'''
817. Linked List Components
1.要求：We are given head, the head node of a linked list containing unique integer values.
    We are also given the list G, a subset of the values in the linked list.
    Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list or one single value.
    head: 0->1->2->3  G = [0, 1, 3] Output: 2
    head: 0->1->2->3->4 G = [0, 3, 1, 4] Output: 2
2.理解：判断list里的元素(为subset of linklist)是否是linklist里的连续或单独元素, 返回数量 
3.类型：list成分判断题
4.方法及方法分析：
time complexity order:  optimization SET method O(N) < 双指针 method O(N2)
space complexity order: optimization SET method O(1) = 双指针 method O(1)
5.edge case: 
    input:
        linklist length?  1 <= N <= 10000 
        node None? N
        node value < > = 0? integer? repeated? range? =>0 / Y / N / [0, N - 1]
        node ordered? N
        G from node value? Y
        G ordered? N
    output：
        int？ Y
    class name: Solution
    focus on time or space?
        
'''

'''
idea： brute force - 双指针 method
Method：
    traversal linklist  #tO(N) *N = tO(N2), sO(1)
        case 1: prev not in G, curr in G: numb_connect + 1  t(N) s(1)
        case 2: pre in G, curr in G: continue  t(N) s(1)
        case 3: pre in G, curr not in G: continue t(N) s(1)
time complex: tO(N2)
space complex:  sO(1)
易错点：本判断句不做操作，继续运行后面的程序，用的是pass! 不是continue！
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G):  #input：linklist，output：numb of connected components
        dummy = prev = ListNode(-1)  # build dummy head for head
        dummy.next = head
        curr = head

        numb_c = 0
        while curr:  # traversal the linklist
            if prev.val not in G and curr.val in G:  # case 1
                numb_c += 1
            elif prev.val in G and curr.val in G:  # case 2
                pass
            elif prev.val in G and curr.val not in G:  # case 3
                pass
            prev = prev.next
            curr = curr.next

        return numb_c

'''
optimization SET method
idea： transfer G list into set 
Method：
    traversal linklist  #tO(1) *N = tO(N), sO(1)
        case 1: prev not in G, curr in G: numb_connect + 1  t(1) s(1)
        case 2: pre in G, curr in G: continue  t(1) s(1)
        case 3: pre in G, curr not in G: continue t(1) s(1)
time complex: tO(N)
space complex: sO(1)
易错点：
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G):  #input：linklist，output：numb of connected components
        dummy = prev = ListNode(-1)  # build dummy head for head
        dummy.next = head
        curr = head

        numb_c = 0
        G_set = set(G)
        while curr:  # traversal the linklist
            if prev.val not in G_set and curr.val in G_set:  # case 1
                numb_c += 1
            elif prev.val in G_set and curr.val in G_set:  # case 2
                pass
            elif prev.val in G_set and curr.val not in G_set:  # case 3
                pass
            prev = prev.next
            curr = curr.next

        return numb_c

A0 = ListNode(0)
A1 = ListNode(1)
A2 = ListNode(2)
A3 = ListNode(3)
A4 = ListNode(4)

A0.next = A1
A1.next = A2
A2.next = A3
A3.next = A4


x = Solution()
print(x.numComponents(A0, [0, 3, 1, 4]))