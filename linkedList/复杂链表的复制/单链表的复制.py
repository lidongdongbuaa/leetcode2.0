# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 9:29
# @Author  : LI Dongdong
# @FileName: 单链表的复制.py

'''
1.要求：
2.类型：
3.方法：
4.边界条件：
'''

'''
思路：只关心new node和它的next，并把next=的节点视为node，然后返回这个节点，再用self替换，
不关系他是怎么来的和上层怎么跟它联系的，
方法：
边界条件：
time complex: 
space complex: 
'''
############单链表的复制###################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def copyList(self, head):
        if head == None:
            return None

        new_node = ListNode(head.val)
        new_node.next = self.copyList(head.next)
        return new_node

############138 复杂链表的复制###################
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visitHash = {}

    def copyRandomList(self, head):
        if head == None:
            return None

        new_node = Node(head.val, None, None)
        self.visitHash[head] = new_node
        new_node.next = self.copyRandomList(head.next) #建立node和next全部完成

        if head.random != None:
            new_node.random = self.visitHash[head.random]
        else:
            pass

        return new_node



A1 = ListNode(1)
A2 = ListNode(2)
A3 = ListNode(3)
A4 = ListNode(4)
A1.next = A2
A2.next = A3
A3.next = A4

x = Solution()
print(x.copyList(A1).next.next.val)