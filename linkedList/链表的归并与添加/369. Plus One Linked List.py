#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 9:47
# @Author  : LI Dongdong
# @FileName: 369. Plus One Linked List.py
''''''
'''
题目分析
1.要求：Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
        You may assume the integer do not contain any leading zero, except the number 0 itself. [1,2,3] -> [1,2,4]
        The digits are stored such that the most significant digit is at the head of the list.
2.理解：给了我们一个链表，用来模拟一个多位数，表头是高位，现在让我们进行加1运算 
3.类型：链表节点求和
4.方法及方法分析：转化为数字法,链表转置法
time complexity order:  链表转置法 O(N) = 转化为数字法 O(N) 
space complexity order: 链表转置法 O(1) < 转化为数字法 O(N)
'''

'''
转化为数字法
思路：把链表保存成整数，整数加1，然后再还原成链表
方法：先求链表长度 tO(N)
    后根据长度，决定每一个node值的位置，乘以相应的分位数；tO(N) sO(1)
    加一；tO(1) 
    然后根据根据之前链表的长度或长度+1来得到确认新数的长度 tO(1)
    再用//法来确定每一位的数，同时合并成新的链表 tO(N) sO(N)
边界条件：
time complex: O(N)
space complex: O(N)
易错点：
'''

'''
链表转置法
思路：先转置链表，变成从个位到高位；从低位迭代到高位，同时对个位加1，若为10，本head.val改为0，下一位继续加1；若不为，终止迭代
方法：先迭代整个链表进行转置；
    i=1, 后对新链表递归，若head.val + i == 10，head.val = 0, 继续下个迭代；若head.val +i !=10, head.val = head.val+ i,终止迭代，返回头节点
    对新链表转置，返回转置后的新链表
边界条件：head.val = 0/最高位变为10，需要加1位数
time complex: tO(N)
space complex: sO(1)
易错点：一定要curr = curr.next
    b = ListNode(2) a = b.next a = ListNode(9) 这样时a.val = 9,但是b.next依然为None,
    即因为python等于号 = 的含义是赋地址，故在a = ListNode(9)后，a获得了新地址，b.next还是原来老a的，故不匹配
    只有next可以链接地址，故在curr = curr.next之前把curr.next = ListNode(1)建立好
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        new_head = None
        while head: #tO(N)
            next_head = head.next
            head.next = new_head
            new_head = head
            head = next_head

        curr = new_head
        while curr: #max is tO(N), sO(1) while的循环是基于+1是否递进
            if curr.val + 1 == 10:
                curr.val = 0
                if curr.next is None:
                    curr.next = ListNode(1) #1 是新添加的，该结束了，不然又一轮while
                    break
                curr = curr.next
            else:
                curr.val = curr.val + 1
                break

        final_head = None
        while new_head: #tO(N)
            next_head = new_head.next
            new_head.next = final_head
            final_head = new_head
            new_head = next_head

        return final_head



