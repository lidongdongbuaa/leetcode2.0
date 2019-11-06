# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 21:57
# @Author  : LI Dongdong
# @FileName: 206. Reverse Linked List.py
''

'''
题目分析
1.要求：reverse a linked list
A linked list can be reversed either iteratively or recursively. Could you implement both?
2.理解：全链表转置
3.类型：链表题,单链表
4.方法及方法分析：iteration法,  recursion法,  backtrack法 
time complexity order: iteration法 O(n) = recursion法 O(n) = backtrack法 O(n)
space complexity order: iteration法 O(1) > recursion法 O(n) > backtrack法 O(n)
'''

'''
iteration法
思路：建立空链头，调整head的指向
方法：链表转置常规方法
边界条件：head == None
time complex: O(n)
space complex: O(1)
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head) :
        prev = None #previous node is None
        curr = head #use the copy of the head (current node, curr）instead of the original head
        while curr:
            #######从头到尾的转置方式###############################
            nextTemp = curr.next #backup next node as nextTemp
            curr.next = prev  # current node points to previous node
            prev = curr     # previous goes forward a step to current head(curr) 's position，深度复制,不是简单的指向改变
            curr = nextTemp # set current node as the backup node 深度复制，不是简单的指向改变
        # Attention: return previous node instead of current node
        return prev



'''
recursion 法
思路：把iterative法中的while替换为recursive
方法：由于head最后为None，故无法作为新生成链表的头进行返回，需要加入new_head作为新变量
故采用init+递归/主函数+递归方法，提出new_head作为新变量，并返回新值
边界条件：head == None
time complex: O(n)
space complex: O(n)

易错点：self.new_head = None，不是 ListNode(0)
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#写法1
class Solution:
    def __init__(self):
        self.new_head = None

    def reverseList(self, head):
        if head == None:
            return self.new_head

        nextTmp = head.next
        head.next = self.new_head
        self.new_head = head
        head = nextTmp
        return self.reverseList(head)

#写法2
class Solution:
    def reverseList(self, head):
        new_head = None
        return self.recursive(head, new_head)

    def recursive(self, head, new_head):
        if head == None:
            return new_head

        nextTmp = head.next
        head.next = new_head
        new_head = head
        head = nextTmp
        return self.recursive(head, new_head)




'''
backtrack法 
思路：利用backtracking的性质，从后往前对linkedlist进行转置
方法：先recursive到末尾，如recursive_end(self, head)所示，然后在backtracking的过程中，进行pointer的改变
难点：递归程序中，如何把转置后的头节点prev返回出来
边界条件：head == None
time complex: O(n)
space complex: O(n)
'''
class Solution:
    def __init__(self):
        self.new_head = None

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    ####下面是只用recursive时的程序，结果返回最后一个head###
    def recursive_end(self, head):
        if head == None or head.next == None:
            return head

        end_head = self.recursive_end(head.next)
        return end_head





head=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)
head.next=b
b.next=c
c.next=d
d.next=e

rl=Solution()
print(rl.reverseList(head).val)