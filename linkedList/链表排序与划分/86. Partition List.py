# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:02
# @Author  : LI Dongdong
# @FileName: 86. Partition List.py

####################### 题目分析 ##########################
'''
1.要求：划分链表为两个部分，小于x的位于大于等于x的之前，并保持原有链表的次序
2.类型：链表题；链表排序与划分
3.方法：Two Pointer Approach；list储存 method
4.边界条件：head为None或单节点时，返回原节点
'''
####################### Two Pointer Approach ##################
'''
思路：用next连接的方法，构成小于x的链和大于等于x的链，之后再串起来
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
方法：建立两个新头，head1，head2，迭代head，val小于3，连接head1；val大于等于3，连接head2。
迭代完毕之后，head1末尾连接head2的头；新头.next才是真正起始点;head2要收尾，即head2.next=None
边界条件：head为None或单节点时，返回原节点
time complex: 核心语句head=head.next,故O(n)
space complex: O(1)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head

        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            if head.val < x:
                before_head.next = head
                before_head = before_head.next
            else:
                after_head.next = head
                after_head = after_head.next
            head = head.next
        after = after.next
        before_head.next = after
        after_head.next = None
        return before.next

####################### list储存 method ##################
'''
思路：遍历链表，把小于x和大于等于x的分别储存进两个list里，后根据这两个list重新构建链表
方法：建立list1，list2，list1储存小于x的数，list2储存大于等于x的数；后分别遍历这两个list建立两个链表，然后拼接这两个链表
边界条件：while为None或单节点时，返回原节点
time complex: O(n)+O(n1)+O(n2)=O(n)+O(n)=O(n)
space complex: O(n)+O(1)+O(n1)+O(n2)=O(n)+O(1)+(n)=O(n)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head

        list1 = []
        list2 = []
        curr = head
        while curr:
            if curr.val < x:
                list1.append(curr.val)
            else:
                list2.append(curr.val)
            curr = curr.next

        bef =  before_head = ListNode(0)
        for elem in list1: #tO(n1)
            new_node = ListNode(elem)
            before_head.next = new_node
            before_head = before_head.next

        aft = after_head = ListNode(0)
        for elem in list2: #tO(n2)
            new_node = ListNode(elem)
            after_head.next = new_node
            after_head = after_head.next

        if list1 == []:
            return aft.next
        elif list2 == []:
            return bef.next
        else:
            bef = bef.next
            aft = aft.next
            before_head.next=aft
            return bef



######################  构造链表  ######################################
A1 = ListNode(1)
A2 = ListNode(4)
A3 = ListNode(3)
A4 = ListNode(2)
A5 = ListNode(5)
A6 = ListNode(2)



A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5
A5.next = A6

X = Solution()
print(X.partition(A1,3).val)
