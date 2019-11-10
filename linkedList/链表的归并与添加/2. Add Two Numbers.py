#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 9:22
# @Author  : LI Dongdong
# @FileName: 2. Add Two Numbers.py
''''''
'''
题目分析
1.要求：You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        (2 -> 4 -> 3) + (5 -> 6 -> 4) -> (7 -> 0 -> 8)
2.理解：两个链表，数字对应的两两相加，不含前导0，即链表结束，数也就结束了；两个链表都非空
    与369题类似，可以深化为怎么求两个整数 (3 -> 4 -> 2) + (4 -> 6 -> 5)的和，即先转置成本题这样，再转置回去
3.类型：链表节点求和
4.方法及方法分析：两两值相加迭代法 转化为数字法
time complexity order: 两两值相加迭代法 O(N)
space complexity order:  两两值相加迭代法 O(N)
'''

'''
两两值相加迭代法
思路：构建新链表，同时迭代两个链表，把两个链表节点值的和构建成新链表的节点值；直到其中一个/两个链表到底
方法: 新建链表，while l1 and l2, 两个链表节点和为新链表的节点值，若为10，则加入下一位，若为某链末尾，则另一个链表下一位加1
边界条件：节点和为10时/节点和为10且为最后一位时
time complex: tO(N)
space complex: sO(N)
易错点：迭代链表(while)时，一定不要忘了head.next = head-->首先就要添加
    此题可以为9+9，跟369加1是不一样的，故curr.next = ListNode(l1.val + l2.val + i - 10)，不要忘记减10
    同样的9+9，在最后，可能出现l1和l2都为None时，这个时候要新建1node添加到链表最后
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addOne(self, head):
        curr = head
        while head:
            if head.val + 1 == 10:
                head.val = 0
                if head.next is None:
                    head.next = ListNode(1)
                    break
                head = head.next
            elif head.val + 1 != 10:
                head.val += 1
                break
        return curr

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = new_head = ListNode(0)
        i = 0
        while l1 and l2: #tO(N), sO(N)
            if l1.val + l2.val + i >= 10:
                curr.next = ListNode(l1.val + l2.val + i - 10)
                i = 1
            else:
                curr.next = ListNode(l1.val + l2.val + i)
                i = 0
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        if i == 0:#tO(1), sO(1)
            if l1 is None:
                curr.next = l2
            elif l2 is None:
                curr.next = l1
        elif i == 1:  #tO(N), sO(N)
            if l1 is None and l2 is not None:
                curr.next = self.addOne(l2)
            elif l2 is None and l1 is not None:
                curr.next = self.addOne(l1)
            elif l1 is None and l2 is None:
                curr.next = ListNode(1)

        return new_head.next

'''
转化为数字法
思路：把两个链表都转化为整数，然后相加得到结果，最后把结果转成链表并转置输出
方法: 使用while遍历链表，每遍历一次，node.val乘以10，同时累加这个结果，得到最后的转化整数；
    相加两个整数；
    把这个整数转化为string；
    遍历这个string的每个elem，再把每个elem转化为int；
    同时再构造为新的链表,然后转置输出！
边界条件：head = None
time complex: O(N) + O(1) + O(1) + O(N) + O(N) = O(N)
space complex: O(1) + O(1) + O(1) + O(N) = O(N)
易错点：算完和之后，结果整数是正常顺序的，而题目要求是倒叙数，故在采用转成string再转int再建链表时，得到的链表也是正常顺序的，故最后需要转置后输出
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def LinkedListToNum(self,head):
        num = 0
        times = 1
        while head:
            num += head.val*times
            head = head.next
            times *= 10
        return num

    def reverse_Linkedlist(self, head):
        if head is None:
            return None #check head is None
        pre = None
        while head:
            next_head = head.next
            head.next = pre
            pre = head
            head = next_head
        return pre

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.LinkedListToNum(l1)
        num2 = self.LinkedListToNum(l2)

        total= num1 + num2
        total_string = str(total)
        pre = new_head = ListNode(0)
        for elem in total_string:
            new_node = ListNode(int(elem))
            pre.next = new_node
            pre = pre.next

        return self.reverse_Linkedlist(new_head.next)

'''
test case
'''
b = ListNode(5)
a = ListNode(5)
x = Solution()
print(x.addTwoNumbers(a,b).val)