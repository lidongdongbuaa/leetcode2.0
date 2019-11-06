#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 19:42
# @Author  : LI Dongdong
# @FileName: 24. Swap Nodes in Pairs.py
''''''
'''
题目分析
1.要求：Given a linked list, swap every two adjacent nodes and return its head.You may not modify the values in the list's nodes, only nodes itself may be changed.
2.理解：每两个node进行转置，不能改变node的值，仅指向可以改变
3.类型：列表转置
4.方法及方法分析：iteration法，list存储法
time complexity order: iteration法 O(N) = list存储法 O(N)
space complexity order: iteration法 O(1) < list存储法 O(N)
'''

'''
list存储法
思路：把链表里的都存到list里，然后两两改变顺序，然后重新建立新的链表
方法：链表先递归存入list，然后用for in(0,len(list),interval)去两两改变顺序(奇偶问题)，然后迭代建立新的链表
边界条件：head = None
time complex: O(N)
space complex: O(N)
易错点：奇偶问题,即if i == len(list_node) - 1
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head) :
        if head == None:
            return None

        curr = head
        list_node = []
        while curr:  #tO(N) sO(N)
            list_node.append(curr.val)
            curr = curr.next

        for i in range(0, len(list_node),2): #tO(N)
            if i == len(list_node) - 1:
                break
            else:
                list_node[i], list_node[i+1] = list_node[i+1], list_node[i] #书写亮点

        dummy = new_head = ListNode(0)
        for elem in list_node: #tO(N) sO(N)
            new_node = ListNode(elem)
            new_head.next = new_node
            new_head = new_head.next

        return dummy.next


'''
iteration 两两转置法
思路：两两转置，备份-改变pointer
方法：打破全转置的一一node转置的思维定势，建立空节点，并指向head,为before；
    保存nexthead,nextnexthead；before->nh,nh->head,head->nnh;
    before = head, head = head.next
边界条件：head = None;只有一个节点；只有两个节点
time complex: O(N)
space complex: O(1)
易错点: 打破全转置的一一node转置的思维定势；while head and head.next
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head) :
        if head == None:
            return None

        if head.next == None:
            return head

        before = pre = ListNode(0)
        before.next = head #建立头节点之前的空节点

        while head and head.next:
            next_head = head.next
            next_next_head = head.next.next
            before.next = next_head
            next_head.next = head
            head.next = next_next_head
            before = head
            head = head.next #or head = next_next_head
        return pre.next





A1 = ListNode(1)
A2 = ListNode(2)
A3 = ListNode(3)
A1.next = A2
A2.next = A3

X = Solution()
print(X.swapPairs(A1).val)




