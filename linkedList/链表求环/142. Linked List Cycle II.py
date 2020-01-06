# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 21:24
# @Author  : LI Dongdong
# @FileName: 142. Linked List Cycle II.py

############  题目分析    ##########################
'''
1.要求：给一个链表，判断是否有环，若有，返回环节点；若无，返回None
Follow-up:Can you solve it without using extra space?
2.理解：判断是否有环，记录环的位置
3.类型：链表题；有环链表
4.方法：hash table method; two pointer running method
5.边界条件：链表为空，返回None
'''
####################### hash table method ##################
'''
思路: 环节点一定是重复点，故把已经读取的node存入一个容器，然后那新的node与容器里的node进行比对
方法: 把每个node值存入hash table(list,set,dic)，迭代新的node，用in判断重复node是否存在，若存在，返回该node
边界条件：链表为None，返回None
循环条件：node不为None
循环范围：
有环条件：若有环，从本链表的头到环交点处；
无环条件：若无环，从本链表的头到尾
循环内容：traverse每一个node，判断若hash table有相同node，返回该node，若无，存入hash table，继续循环
循环结束后：返回None
返回条件：在一个循环内hash table有相同的node，返回node；循环完毕，无环，返回None
time complex: traverse：循环体中语句的执行次数，n*O(1)(hash table 检查in) + n*O(1)(next) + n*O(1)(position)= O(n)
space complex: 原链表O(1)+hash table O(n) = O(n+1)=O(n)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        hash_table = {}
        #hash_table = set()
        #hash_table = []
        while head:
            if head in hash_table:
                return head
            hash_table[head] = 1
            #hash_table.add(head)
            #hash_table.append(head)
            head = head.next
        return None

####################### fast-slow pointer running method ##################
'''
思路: 环节点是分界点，若两个速度不同的pointer迭代时，相遇处和环节点处有数学联系
方法: 使用两个速度不同pointer，从起点开始走，有环会相遇,然后从起始点和相遇点分别以速度1开始走，
再次相遇点为交叉点（数学证明如下）；无环不相遇
边界条件：链表为None，返回None
循环数量：2
循环条件：pointer2及pointer2.next是否为None (快的pointer是否迭代完成链表）/ 新迭代中pointer1 是否相遇pointer2
循环范围：若有环，从pointer2的头到与pointer1的相交点；若无环，从pointer2的头到pointer2的尾 / 从头到交叉点
循环内容：两个pointer分别从起点开始迭代，pointer1速度为1 node/step，pointer2速度为2 node/step，有环时，pointer1=pointer2，则返回true，
无环时，迭代完毕，不满足循环条件，退出循环 /从起始点和相遇点分别以速度1开始走，再次相遇点为交差点
循环结束后：返回None / 返回相遇点，即为交叉点
返回条件：
有环时：在pointer1的一个循环内pointer1=pointer2，返回pointer；
无环时：pointer1循环完毕以后，无环，返回None
time complex: 
若无环，T(n)=2*n/2 (fast 迭代整个链表，.next.next为*2)=O(n)；
若有环，T(n)=2*n/2 +2*k/2=O(n)(k最多为闭环内的长度，N + K = length linkedlist);
Number of iterations=non-cyclic length=N
Number of iterations=almost cyclic length= K 
space complex: O(1)

数学证明： 
证明1:是否有环
    设非环部分为L1，环部分为L2，假设走s步后相交，可以得出(1)有解
    (s - L1) mod L2 = (2s - L1) mod L2  (1) 
    由(1)可以得到
    s - L1 = n*L2 + p  (2)(p是余数)
    2s - L1 = m*L2 + p  (3)
    由(2),(3)可以得到
    s = (m - n)L2  (4)
    由于m-n是可变的，故(4)显然有解
证明2：是否1圈内可以追上，即算法复杂度为O(N)
    当L2 >= L1 时，假设一圈内追上（s<L1+L2)，看是否可以满足(4)
        故令 s = L1 + k = L2，此时可以满足(4)，即条件成立，可以追上
    当L1 > L2 时，假设一圈内追上（s<L1+L2)，看是否可以满足(4)
        故令 s = L1 + k = n1*L2，此时满足(4)
        
证明3：求第一个交点位置
    设p1为环交点到追击点的长度，p2为追击点到环交点的长度，由(4):
    （m - n - 1)L2 + L2 = s -> (m - n - 1)L2 + p1 + p2 = L1 + p1
    -> (m - n - 1)L2 + p2 = L1这个式子表明链表中不包括环的长度 等于 相遇点到第一个相交点的长度加上环的长度的整数倍。
 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        if head == None:
            return None

        pointer1 = head
        pointer2 = head
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                break
        else:
            return None

        pointer1 = head
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
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
print(rl.detectCycle(A1))