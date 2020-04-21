# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 7:30
# @Author  : LI Dongdong
# @FileName: 160. Intersection of Two Linked Lists.py
############  题目分析    ##########################
"""
1.要求：找出两个单链表的intersection；无intersection时返回null；
链表保持原有结构；假设链表无环; O(n) time and use only O(1) memory
2.理解：两个单链表的intersection，即地址相同的两个节点，即nodeA == nodeB，此时nodeA.val=nodeB.val,nodeA.next=nodeB.next
(注意：val相同，next相同的两个节点的地址不一定相同，故不一定相等)
保持原有结构->不构建新的链表；O(1) memory->iterative method;
3.类型：链表题；两单链表；找交点
4.方法：brute force;hash table;reduce gap;双指针-数组
5.边界条件：链表为None，返回None
"""

########################   brute force   ##########################
'''
本方法的time complex 是O(mn), leetcode超时，不符合题意
思路：
for each node a in list A, traverse the entire list B and check if any node
in list B coincides with a
方法：
边界条件：链表为None，为节点
内外两个while循环（for循环需要计算list长度），不断迭代，遇到相同地址的则返回node，
全不相同则返回None
time complex: 设m，n为两段的长度，O(mn)
space complex: O(1)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        while headA:
            currB = headB
            while currB:
                if headA == currB:
                    return headA
                else:
                    currB = currB.next
            headA = headA.next
        return None

###########################  Hash Table  ##############################
'''
新方法
思路：把A的各个节点/节点的地址存入存储结构，然后traverse各个B节点，看看有没有相同的
方法：
边界条件：链表为None，为节点
A中每一个node都不一样，故可以用list/hash table(dic/set)实现存储结构，
但是由于hash table的time complexity为O(1), 而list为O(n), 故使用hash table实现，然后traverse B中node
用 X in hash table 来实现判断
time complex: 设m，n为两段的长度，添加时O(m)，迭代时O(n)，查询时O(1),故总计为O(m+n+1) 
而用list的查询time complex 时O(n),总计为O(m+2n)
->疑问？list超时，但是他与two pointer method 1 相比看起来差别不大
->可能因为tpm 1的最大是O(2m+2n)，但是平时远未到，而用list，一定是O(m+2n)
space complex: max(O(m),O(n))
'''
class Solution:
    class Solution:
        def getIntersectionNode(self, headA, headB):
            if headA == None or headB == None:
                return None
            hash_table = {}
            # or hash_table = set()
            while headA:
                hash_table[headA] = 1
                #hash_table.add(headA)
                headA = headA.next
            while headB:
                if headB in hash_table:
                    return headB
                else:
                    headB = headB.next
            return None
'''
如下代码有错误，因为continue，故headB = headB.next 没有运行
                else:
                    continue
                headB = headB.next
'''
######################## reduce gap method ##########################
'''
思路：分别从两段相同长度的起始点开始往后iterative
方法：求长度差异->移动较长段的pointer到与较短段相同的长度处-》两条链表一起跑，
最多跑公共长度，找交点
time complex: 设m，n为两段的长度，O(m)+O(n) + O(m-n) + min(O(m),O(n)) = O(n)
space complex: O(1)
'''
class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        currA=headA
        currB=headB

        lengthA=0
        while currA:
            lengthA+=1
            currA=currA.next
        lengthB=0
        while currB:
            lengthB+=1
            currB=currB.next

        if lengthA > lengthB:
            gap = lengthA - lengthB
            while gap:
                headA=headA.next
                gap-=1
            while lengthB:
                lengthB -= 1
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
            return None

        elif lengthA == lengthB:
            while lengthA:
                lengthA -= 1
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
            return None

        elif lengthA < lengthB:
            gap = lengthB - lengthA
            while gap:
                headB=headB.next
                gap-=1
            while lengthA:
                lengthA -= 1
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
            return None

####################### Two pointer method 1 ###########################
'''
思路：同时迭代A和B，A运行完接上B运行，B运行完接上A运行，过程中，如相遇则为交点，如不相遇则返回None
方法：设计循环，判断条件为A长+B长的循环次数，A循环完后为None时，用赋值拼接连接B，B同理，当headA=headB时跳出返回head，当循环完成之后都无，则返回None
time complex: 设m，n为两段的长度，0(m)+O(n)+O(m)+O(n) = 0(2m+2n)=O(n)
space complex: O(1)

注：赋值拼接和next拼接的区别
赋值拼接以后，未改变原有结构；而如果是用.next=进行拼接，则改变了原有结构。
同时由于是A拼B，B拼A，那么赋值拼接结果是两个分段AB,BA,而next拼接是环 A-B-A
'''
class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        currA=headA
        currB=headB
        lengthA = 0
        lengthB = 0
        while currA:
            lengthA += 1
            currA = currA.next
        while currB:
            lengthB += 1
            currB = currB.next

        sum_length = lengthA + lengthB
        tempA=headA
        tempB=headB
        while sum_length:
            if not headA:
                headA = tempB
            if not headB:
                headB = tempA
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            sum_length -= 1
        return None

#######################  Two pointer method 2 ###########################
'''
Two pointer method 1 的优化版
思路：与Two pointer method 1相同
方法：while判断条件改为headA!=headB，当有交叉点且运行到交叉点时，while不满足，跳出，返回交叉点(headA)；
当没有交叉点时，递归完两个分段，两个指针都指向的分段的末尾（curA = None,curB= None)，while不满足，跳出，返回交叉点（headA=None）
while判断条件不能用headA==None or headB==None,因为traverse到拼接点时，headA or headB也会为None;
用and时，若有交叉点，还要添加其他条件进行返回交差点。故用 while curA != curB:是最好的。
time complex: 设m，n为两段的长度，设m，n为两段的长度，0(m)+O(n)=O(m+n)=O(n)
space complex: O(1)

注：新型书写方式：
            if curA:
                curA = curA.next
            else:
                curA = headB
            与
            curA = curA.next if curA else headB
            相同
'''
class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        curA = headA
        curB = headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
            curB = curB.next if curB else headA
        return curA

######################  Two pointer method 3  #######################################
'''
本方法由于用next连接了A和B，改变了原链表的结构，故不符合题意
思路：A尾连B头，B尾联A头，A,B两头同时iterative，相遇的时候即交点，不相遇则没有交点
方法：A pointer移动到末尾，后连接B头；B同样做->同时从A,B头开始移动，最多移动m+n次，相等则返回node，全部不能则返回None
time complex: 设m，n为两段的长度，O(m)+O(n) + max(O(n),O(m)) = O(n)
space complex: O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        currA = headA
        currB = headB
        lengthA = 0
        lengthB = 0
        while currA:
            lengthA += 1
            prevA = currA
            currA = currA.next
        while currB:
            lengthB += 1
            prevB = currB
            currB = currB.next

        prevA.next = headB
        prevB.next = headA

        sum_length = lengthA + lengthB
        while sum_length:
            sum_length -= 1
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

######################  构造交叉链表  ######################################
A1 = ListNode(4)
A2 = ListNode(1)

B1 = ListNode(5)
B2 = ListNode(0)
B3 = ListNode(1)

C1 = ListNode(8)
C2= ListNode(4)
C3= ListNode(5)



A1.next = A2
A2.next=C1
C1.next=C2
C2.next=C3

B1.next=B2
B2.next=B3
B3.next=C1


rl = Solution()
rl.getIntersectionNode(A1,B1)