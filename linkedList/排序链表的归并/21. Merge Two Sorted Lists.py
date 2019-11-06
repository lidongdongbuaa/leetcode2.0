# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 11:23
# @Author  : LI Dongdong
# @FileName: 21. Merge Two Sorted Lists.py

######################## 题目分析    #################
'''
1.要求：Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
2.类型：链表题；合并题
3.方法：Iterative法；recursion法
4.边界条件：l1 or l2 = None
'''
######################## Iterative法  ################
'''
思路：先边界，比较大小，然后用next连接
方法：建立新头，比较大小后，next连接
边界条件：l1 = None or l2 = None
time complex: O(m+n)
space complex: O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        new_node = curr = ListNode(0)
        while l1 or l2:
            if (l2 == None and l1 != None) or (l1 != None and l1.val < l2.val):
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            elif (l1 == None and l2 != None) or (l2 != None and l2.val <= l1.val):
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        return new_node.next
######################## Iterative法2  ################
'''
思路：先边界，比较大小，然后用next连接
方法：建立新头，比较大小后，next连接，最后剩下的不用比较，直接连接
边界条件：l1 = None or l2 = None
time complex: O(m+n)
space complex: O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        new_node = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1 == None:
            curr.next = l2
        else:
            curr.next = l1

        return new_node.next

######################## recursion 1  #################################
'''
思路：建立新的链表，next指向l1或l2中较小的那个
方法：recursion法
边界条件：l1 = None and l2 = None
time complex: O(m+n)
space complex: O(m+n)

过程分析：先逐步向下构筑好new_head:A->B->C->D->E->F,new_head指向F,l1和l2指向末尾，结尾判断条件是 l1 = None and l2 = None，递归到达最底层
然后，由于return，迭代开始往上返回，又由于return 无返回值，故只是过程的往上层的返回，没有返回值返回。同时l1,l2,new_head的pointer也返回到上一层的值
最终l1,l2,new_head都恢复到刚定义的指向，但是此时其后的链表都已经随着之前的逐步向下的递归发生了改变
更重要的是，这个过程中，由于A->B->C->D->E->F已经搭建好，故返回时，new_head整个链表是不变的，变得只是pointer的指向，逐步向前的指向。
例如 self.recursive(l1.next, l2, new_head.next)返回到上一层之后，l1,l2,new_head自然而然变成本层的原来的指向，而不是递归到最后的指向。
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        new_head = ListNode(0)
        self.recursive(l1, l2, new_head)
        return new_head.next

    def recursive(self, l1, l2, new_head):
        if l1 == None and l2 == None:
            return

        if (l2 == None and l1 != None) or (l1 != None and l1.val < l2.val):
            new_head.next = l1
            self.recursive(l1.next, l2, new_head.next)

        if (l1 == None and l2 != None) or (l2 != None and l2.val <= l1.val):
            new_head.next = l2
            self.recursive(l1, l2.next, new_head.next)

######################## recursion 1 原始版 #########################
'''
问题：存在很多无用的return 变量
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        curr = new_head = ListNode(0)
        self.recursive(l1, l2, new_head)
        return curr.next

    def recursive(self, l1, l2, new_head):
        if l1 == None and l2 == None:
            return new_head

        if (l2 == None and l1 != None) or (l1 != None and l1.val < l2.val):
            new_head.next = l1
            new_head = new_head.next
            m=self.recursive(l1.next, l2, new_head)
            return m


        if (l1 == None and l2 != None) or (l2 != None and l2.val <= l1.val):
            new_head.next = l2
            l2 = l2.next
            new_head = new_head.next
            n = self.recursive(l1, l2, new_head)
            return n



######################## recursion 2  ###########
'''
思路：基于原有链表，改变原有链表的next指向，而不是建立新的链表
方法：recursion法，其实是backtrack
边界条件：l1=None/l2=None
time complex: O(m+n)
space complex: O(m+n)
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val < l2.val:
            p = self.mergeTwoLists(l1.next, l2)
            l1.next = p
            return l1 #发现只要不把pointer后移，即x=x.next,pointer一直在首位的，这样，返回该pointer就好，不用一开始复制pointer
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


A1 = ListNode(1)
A2 = ListNode(2)
A3 = ListNode(3)
A1.next = A2
A2.next = A3


B1 = ListNode(2)
B2 = ListNode(4)
B3 = ListNode(5)
B1.next = B2
B2.next = B3


X = Solution()
print(X.mergeTwoLists(A1,B1).val)