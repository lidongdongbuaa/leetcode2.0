# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 17:09
# @Author  : LI Dongdong
# @FileName: 23. Merge k Sorted Lists.py
''

'''
题目分析
1.要求：Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
2.理解: 合并多个链表
3.类型：链表题，合并链表
4.方法：list储存重构法；迭代法两两合并；递归法两两合并；一一合并；优先队列/堆
time complexity order: 迭代法两两合并 O(Nlogk)= 递归法两两合并 O(Nlogk) = 优先队列/堆 O(Nlogk) < list储存重构法 O(NlogN) < 一一合并 O(Nk)
space complexity order: 迭代法两两合并 O(1) = 一一合并 O(1) < 递归法两两合并 O(N) = list储存重构法 O(N) = 优先队列/堆 O(N)
'''

'''
brute force : list储存重构法
思路：用list储存所有的节点值，排序，然后重新构建新的链表
方法：迭代各个链表的各个节点，保存，排序，重新构建
边界条件：list == []
time complex: O(NlogN); N is the total number of nodes
space complex: O(N)
易错点：链表的pointer改变的空间复杂度为O(1)，新建链表的空间复杂度是O(n)
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list[ListNode]):
        if list == []:
            return []

        sum_node = [] #sO(n)
        for ListNode_son in lists: #tO(N)
            while ListNode_son:
                sum_node.append(ListNode_son.val)
                ListNode_son = ListNode_son.next

        sum_node.sort() #tO(NLogN) sO(N)

        dummy = curr = ListNode(0)
        for elem in sum_node:   #tO(N) sO(N)
            new_node = ListNode(elem)
            curr.next = new_node
            curr = curr.next

        return dummy.next

'''
迭代法两两合并，即归并排序
思路：两两合并，与依次合并相比，无重复排序节点，
方法：
边界条件：list = [] return None
time complex: O(Nlogk) where k is the number of linked lists.
space complex: O(1)
易错点：list = [] return None 而不是[]; while interval < length:之后记住
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeLists(self, head1, head2): #tO(N)，sO(1)
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        dummy = new_head = ListNode(0)
        while head1 and head2:
            if head1.val > head2.val:
                new_head.next = head2
                head2 = head2.next
            else:
                new_head.next = head1
                head1 = head1.next
            new_head = new_head.next

        if head1 != None:
            new_head.next = head1
        else:
            new_head.next = head2
        return dummy.next

    def mergeKLists(self, lists: list[ListNode]):
        if lists == []:
            return None

        length = len(lists)
        interval = 1
        while interval < length: #迭代目标的间隔，即i和i+1的间隔
            for i in range(0, length - interval, 2*interval): #tO(logk)，（k is the number of linked lists，2**m = k，故为log(2)k,简写为logk. sO(1)
                #数值范围内，要保证取到的数i的i+interval是存在的，故要length - interval；每两个迭代目标取一个数，故取值间隔是2倍的interval，
                lists[i] = self.mergeLists(lists[i], lists[i+interval]) #通过加interval实现了最后一位数的操作
            interval = 2*interval
        return lists[0]

'''
递归法两两合并,即归并排序
思路：两两合并，与依次合并相比，无重复排序节点，
方法：
边界条件：list = [] return None
time complex: O(Nlogk) 
    where k is the number of linked lists，N is the number of node
    T(k) = O(1), k = 1（即只有一个链表）；= 2T(k/2) + O(N)，k>=2
    O(n)是合并含有N个node所需的时间，设为cN，因此：
    T(k) = 2T(k/2) + cN = 2^2T(k/2^2) + 2cN = 2^mT(k/2^m) + mcN
    又因为此时 到达最低点，k/2^m=1 -> k=2^m->m=log(2)k
    化简后，T(k)= NO(1) + log(2)k * cN = O(log(2)k *N)= O(Nlogk)
space complex: O(N) #递归的复杂度为O(N),用栈存储
易错点：
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeLists(self, head1, head2): #tO(N)，sO(1)
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        dummy = new_head = ListNode(0)
        while head1 and head2:
            if head1.val > head2.val:
                new_head.next = head2
                head2 = head2.next
            else:
                new_head.next = head1
                head1 = head1.next
            new_head = new_head.next

        if head1 != None:
            new_head.next = head1
        else:
            new_head.next = head2
        return dummy.next

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) > 1:
            mid = len(lists) // 2
            head1 = lists[:mid]
            head2 = lists[mid:]

            sub_head1 = self.mergeKLists(head1)
            sub_head2 = self.mergeKLists(head2)

            return self.mergeLists(sub_head1, sub_head2)


'''
优先队列/堆
思路：利用优先队列中，数值小的在上面，优先pop出的性质进行合并
方法：
边界条件：list = [] return None
time complex: O(Nlogk) 
    where k is the number of linked lists.
    The comparison cost will be reduced to O(logk).O(logk) for every pop and insertion to priority queue. 
    But finding the node with the smallest value just costs O(1) time.
    There are Nnodes in the final linked list.
space complex: O(N)
    O(n) Creating a new linked list costs O(n) space.
    O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).
易错点：leetcodeText400AG Approach 3答案只适用于python2，故修改如下
'''

from heapq import heappop, heappush

# new defined wrapper class
class ListNodeWrapper(object):
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data.val < other.data.val


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        trav = dummy = ListNode(0)
        heap = []
        for ll in lists:# tO(k)
            if ll:
                self.heappushNode(heap, ll)

        while heap: # tO(N)，sO(N)
            # node = heappop(heap)[1] # removed
            node = heappop(heap).data  # added
            trav.next = node
            trav = trav.next
            if trav.next:
                self.heappushNode(heap, trav.next)

        return dummy.next

    def heappushNode(self, heap, node):
        # heappush(heap, (node.val, node)) # removed
        heappush(heap, ListNodeWrapper(node))  # added


'''
一一合并
思路：一一合并
方法：第一个与第二个合并作为新第一个，新第一在与第三合并作为新新第一个...由此循环
边界条件：list = [] return None
time complex: O(Nk) 
    k is the number of linked lists.
space complex: O(1)
易错点：合并并作为新的node，lists[0] = self.mergeLists(lists[0],lists[i])
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeLists(self, head1, head2):  # tO(N)，sO(1)
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        dummy = new_head = ListNode(0)
        while head1 and head2:
            if head1.val > head2.val:
                new_head.next = head2
                head2 = head2.next
            else:
                new_head.next = head1
                head1 = head1.next
            new_head = new_head.next

        if head1 != None:
            new_head.next = head1
        else:
            new_head.next = head2
        return dummy.next

    def mergeKLists(self, lists):
        if lists == []:
            return None

        for i in range(1, len(lists)):# tO(K)，sO(1)
            lists[0] = self.mergeLists(lists[0],lists[i])
        return lists[0]



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

C1 = ListNode(1)
C2 = ListNode(2)
C3 = ListNode(3)
C1.next = C2
C2.next = C3


D1 = ListNode(2)
D2 = ListNode(4)
D3 = ListNode(5)
D1.next = D2
D2.next = D3

E1 = ListNode(1)
E2 = ListNode(2)
E3 = ListNode(3)
E1.next = E2
E2.next = E3


F1 = ListNode(2)
F2 = ListNode(4)
F3 = ListNode(5)
F1.next = F2
F2.next = F3

x = Solution()
x.mergeKLists([A1,B1,C1,D1,E1,F1])