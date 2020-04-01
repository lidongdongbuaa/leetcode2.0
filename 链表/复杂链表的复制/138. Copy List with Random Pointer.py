# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 9:21
# @Author  : LI Dongdong
# @FileName: 138. Copy List with Random Pointer.py

#138. Copy List with Random Pointer

#####################  题目分析    ##################
'''
1.要求：each node of linked list contains an additional random pointer which could
point to any node in the list or null;return a deep copy of the list
2.类型：链表; deepcopy
3.方法：核心问题是在建立新的node及链表的时候，如何保证完整存储和建立random关系；
方法一：建立新链表时dic对两个链表node之间的对应关系的保存，利用原链的random关系，映射到新链上
方法二：在原链上插空建立新链，这样新的插空链有了next关系，原链的random关系也能通过next关系建立到新链上
4.边界条件: 链表为None，返回None
'''

########################   iterative + hash table   ###########
'''
思路：用常规方法复制并构建新的val和next关系，再用容器储存并复制新的random的关系;
先知道a链中a1->a3的关系，又知道用容器记录相对应的b链中，a1->b1,a2->b2，a3->b3的关系，故知道b1->b3
方法：先构建新链表的val和next：遍历旧链表，用常规方法构建新链表，val相等，满足next关系，用dic储存新旧node的地址对应关系；
后构架新链表的random：遍历旧链表，如果旧node有random，找到旧node对应的旧random，然后在dic里找到旧random对应的新node地址，然后用新node连接这个旧random对应的新node地址，
使这个新node具有了新random；返回新链表
边界条件：head = None，return None;
time complex: while:O(n)+while:O(n) = O(n)
space complex: O(1)+O(n)+(1)=O(n)
'''

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        node_map = {}
        pre = new_node = Node(0, None, None)
        curr = head
        while curr:
            temp_node = Node(0, None, None)
            temp_node.val = curr.val
            new_node.next = temp_node
            new_node = new_node.next
            node_map[curr] = new_node
            curr = curr.next

        curr = head
        temp_head = pre.next
        while curr:
            if curr.random:
                curr_random = curr.random
                new_node_random = node_map[curr_random]
                temp_head.random = new_node_random
            temp_head = temp_head.next
            curr = curr.next
        return pre.next

########################  Iterative with O(1) Space   ###########
'''
思路：插空法建立新链node和新链的next，然后基于next和原链random建立新链random
方法：在原链上做文章，对原有链AAAA进行插空，变成ABABABAB,再根据AAA对ABABAB进行next和random关系建立，最后A,B进行分离
边界条件：head = None，返回None
time complex: O(n)
space complex: O(1)
'''

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, None,None)
            next_head = curr.next
            curr.next = new_node
            curr = next_head
            new_node.next = curr

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        #关键是：1.备份新头 2.判断老头退出条件
        new_head = new_node = head.next
        while head.next:
            head.next = head.next.next
            head = head.next
            if head == None:
                new_node.next = None
                break
            new_node.next = head.next
            new_node = new_node.next

        return new_head
########################  Recursive + hash table 1  ###########
'''
思路：先打基础，即建立node和其next，返回node；然后考虑random的问题，与iterative + hash table法相似
方法：
按照建立常规链表的方法（建立node，然后next），先建立headA的nodeA，然后进行next，然后return这个node
由于递归，此过程先全部进行完毕，直到headA = None
然后考虑random的问题
    1. 为了random找到对应的值（一定是next出现过的值），在建立node后，立马就用dic存储head和node关系
    2. 轮到复制建立nodeA的random时，先确定这个headA的random的对应headB，
    然后用dic确定headB的对应nodeB，再联系nodeA和nodeB。
    即headA与nodeA对应，headB与nodeB对应，headA.random = headB => nodeA.random = nodeB
    注意：new_node.random = self.visitHash[head.random]其实是利用了递归的性质，即在上一步 new_node.next = self.copyRandomList(head.next)结束后
    ，self.visitHash已经扩充完毕，如果不是这样，那么self.visitHash[head.random]时，可能在dic中找不到head.random这个key

结束条件->判断是否node已有，若无，则新建->同时建立next和random连接
边界条件：head=None,返回None；dic里面不能有None
实际流程分析：结束条件->判断是否node已有，若无，则新建->建立next->建立random连接
time complex: O(n)
space complex: O(n)
'''
class Solution:
    def __init__(self):
        self.visitHash = {}

    def copyRandomList(self, head):
        if head == None:
            return None

        new_node = Node(head.val, None, None)
        self.visitHash[head] = new_node
        new_node.next = self.copyRandomList(head.next) #建立node和next全部完成

        if head.random != None:
            new_node.random = self.visitHash[head.random]
        else:
            pass

        return new_node
########################  Recursive + hash table 2  ###########
'''
leetcode标准答案
思路：建立链表的常规思路，先判断是否存在，存在则返归dic中保存的对应复制的值；不存在则建立node，再同时建立next和random；
方法：为了random建立的dic，没有就建立，有就返回
time complex: O(n)
space complex: O(n)
'''
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visitHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        if head in self.visitHash:
            new_head = self.visitHash[head]
            return new_head

        if head not in self.visitHash:
            new_head = Node(head.val,None,None)
            self.visitHash[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
            return new_head


class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

########################  Recursive + hash table 3 ###########
class Solution:
    def __init__(self):
        self.visitHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        node = self.dp(head)
        return node


    def dp(self,head):
        if head == None:
            return None

        if head in self.visitHash:
            return self.visitHash[head]

        node = Node(head.val, None, None)

        self.visitHash[head] = node

        node.next = self.dp(head.next)
        node.random = self.dp(head.random)

        return node

########################  Recursive + hash table 4  ###########
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        visitHash = {}
        node = self.dp(head,visitHash)
        return node


    def dp(self,head,visitHash):
        if head == None:
            return None

        if head in visitHash:
            return visitHash[head]

        node = Node(head.val, None, None)

        visitHash[head] = node

        node.next = self.dp(head.next, visitHash)
        node.random = self.dp(head.random, visitHash)

        return node



######################  构造链表  ######################################
A1 = Node(1,Node,Node)
A2 = Node(2,Node,Node)
A1.next = A2
A1.random = A2
A2.next = None
A2.random = A2


X = Solution()
print(X.copyRandomList(A1))





