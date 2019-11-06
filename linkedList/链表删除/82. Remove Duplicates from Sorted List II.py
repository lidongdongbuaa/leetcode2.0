#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 8:24
# @Author  : LI Dongdong
# @FileName: 82. Remove Duplicates from Sorted List II.py
''''''
'''
题目分析
1.要求：Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
2.理解：删除排序链表中重复的值，不留本值
3.类型：链表删除
4.方法及方法分析：dic保存法，next跳跃法
time complexity order: dic保存法O(N) = next跳跃法O(N)
space complexity order: next跳跃法O(1) < dic保存法O(N)
'''

'''
dic保存法-也可以用于非排序链表
思路：利用dic可以保存数值出现次数的功能，选出没有二次及多次出现的node，并重新构建listNode
方法：迭代链表，同时保存到dic中，key为node.val，value为出现次数；后迭代dic，重新构建链表
边界条件：head = None / 不重复的可能为空，返回None
time complex: O(N)
space complex: O(N)
易错点：head = head.next忘记写；建立dummy防止dic不重复的为空；for key,value in dic.items() 循环链表
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        node_dic = {}
        while head: #tO(1)*N = O(N)
            if head.val not in node_dic:
                node_dic[head.val] = 1 #tO(1)
            else:
                node_dic[head.val] += 1
            head = head.next #tO(1)

        dummy = prev = ListNode(0)
        for key, value in node_dic.items(): #tO(N)，sO(N)
            if value == 1:
                new_node = ListNode(key)
                prev.next = new_node
                prev = prev.next
            else:
                pass
        return dummy.next

'''
next跳跃法
思路：建立dummy，迭代链表，并建立小的循环，迭代到不重复的数值，用变量记录是否重复，后用next连接,与203相似
方法：dummy连接head，while迭代链表，并再用一个while去寻找不重复的node，找到后用next连接
边界条件：head = None/node.next node可能为空
time complex: O(N)
space complex: O(1)
易错点：带xx.val一定要判断xx存在；出现1-3-3-3-4-4-5的情况，
        故要用新变量记录是否有重复的情况，若存在重复，则prev.next也是重复数字，故prev.next到下下一位,实现了next跳过已知重复值的步骤，再迭代，看下一个node是不是新重复值；
        ;只有prev.next！= prev.next.next,并且prev.next不是经过next重复值得到的时，才可以决定prev是否要移到下一位，完成了prev向前递进的过程
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        dummy = prev = ListNode(0)
        prev.next = head
        repeatNum = 0
        while prev:#tO(1)*N = O(N)，sO(1)
            while prev.next and prev.next.next and prev.next.val == prev.next.next.val:
                repeatNum = 1
                prev.next =prev.next.next
            if repeatNum == 1:
                prev.next = prev.next.next
                repeatNum = 0
            else:
                prev = prev.next
        return dummy.next

