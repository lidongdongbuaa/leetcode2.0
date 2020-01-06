# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 11:53
# @Author  : LI Dongdong
# @FileName: 141. Linked List Cycle.py

############  题目分析    ##########################
'''
1.要求：给一个链表，判断是否有环，有环返回True，无环返回False；pos代表tail connects,-1代表无环
2.理解：判断链表是否有环
3.类型：链表题；有环链表
4.方法：hash table method；fast-slow pointer running method；
5.边界条件：链表为None，返回False
'''

####################### hash table method ##################
'''
思路: 环节点一定是重复点，故把已经读取的node存入一个容器，然后那新的node与容器里的node进行比对
方法: 把每个node都存入hash table，判断重复node是否存在
边界条件：链表为None，返回False
循环条件：node不为None
循环范围：若有环，从本链表的头到环交点处；若无环，从本链表的头到尾
循环内容：traverse每一个node，判断若hash table有相同node，返回Ture，若无，存入hash table，继续循环
循环结束后：返回False
循环返回条件：
有环情况：在一个循环内hash table有相同的node，返回true；
无环情况：循环完毕，无环，返回false
time complex: traverse：循环体中语句的执行次数，n*O(1)(hash table 检查in) + n*O(1)(next) = O(n)
space complex: 原链表O(1)+hash table O(n) = O(n+1)=O(n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        hash_table = set()
        #hash_table = {}
        #position = 0
        while head:
            if head in hash_table:
                return True
            hash_table.add(head)
            #hash_table[head] = position
            head = head.next
            #position += 1
        return False

####################### fast-slow pointer running method ##################
'''
思路: 环节点是分界点，若两个速度不同的pointer迭代时，相遇处和环节点处有关系
方法: 使用两个速度不同pointer，从起点开始走，有环会相遇，无环不相遇
边界条件：链表为None，返回False
循环条件：pointer2及pointer2.next是否为None (快的pointer)
循环范围：若有环，从pointer2的头到与pointer1的相交点；若无环，从pointer2的头到pointer2的尾
循环内容：两个pointer分别从起点开始迭代，pointer1速度为1 node/step，pointer2速度为2 node/step，有环时，pointer1=pointer2，则返回true，
无环时，迭代完毕，不满足循环条件，退出循环
循环结束后：返回false
循环返回条件：问题有几种分类情况就有几个返回条件。
有环情况：在pointer1的一个循环内pointer1=pointer2，返回true；
无环情况：pointer1循环完毕以后，无环，返回false
time complex: 
若无环，T(n)=2*n/2 (fast 迭代整个链表，.next.next为*2)=O(n)；
若有环，T(n)=2*n/2 +2*k/2=O(n)(k最多为闭环内的长度，N + K = length linkedlist);
Number of iterations=non-cyclic length=N
Number of iterations=almost cyclic length= K 
space complex: O(1)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        pointer1 = head
        pointer2 = head
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return True
        return False

######################  构造交叉链表  ######################################
A1 = ListNode(1)
A2 = ListNode(2)

# B1 = ListNode(5)
# B2 = ListNode(0)
# B3 = ListNode(1)
#
# C1 = ListNode(8)
# C2= ListNode(4)
# C3= ListNode(5)


A1.next = A2
A2.next = A1



rl = Solution()
print(rl.hasCycle(A1))