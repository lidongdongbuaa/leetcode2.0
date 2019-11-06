# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 9:17
# @Author  : LI Dongdong
# @FileName: 92. Reverse Linked List II.py
''''''
'''
题目分析
1.要求：reverse a linked list from m to n in one-pass. 1 ≤ m ≤ n ≤ length of list.
2.理解：one pass is a streaming algorithm which reads its input exactly once, in order.
time = O(n), space < O(n),即按次序读每个数
3.类型：链表题,单链表
4.方法及方法分析：iteration
time complexity order: 
space complexity order:
'''

'''
iteration法
思路：找到需要转置的部分的头尾；进行转置；连接原头-转置部分-原尾
方法：分三段，前段，需要转置的中段，后端
边界条件：head == None
time complex: O(n)
space complex: O(1)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #首先考虑为空
        if head == None:
            return None

        curr, prev = head, None

        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m-1, n-1

        con, tail = prev, curr

        while n:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev #单个节点状况
        tail.next = curr
        return head


'''
backtrack法
思路：改变原有链表的结构，设计前后两个pointer，一个在m，一个在n，m和n的值进行交换，后向中间逼近
方法：利用回溯去模拟从n到中央点的过程，在这个过程中，对m和n的值进行交换，比如1和4位的值进行调换，但是next关系不变
边界条件：head == None
time complex: O(n) since we process all the nodes at-most twice.Once during the normal recursion process and once during the backtracking process. 
space complex: O(n) in the worst case when we have to reverse the entire list. This is the space occupied by the recursion stack.
易错点：self.left.val, right.val = right.val, self.left.val / n == 1 /m > 1
'''
#写法1
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        self.left = head
        right = head
        self.stop = False

        self.recurseAndReverse(right, m, n)
        return head #right也可

    def recurseAndReverse(self,right, m, n):
        #n代表right node的目前为止，m代表left node的目前为止
        #n比m大，故以n到达位置为判断标准，进行return
        if n == 1:
            return

        right = right.next

        if m > 1:
            #m同时向前进
            self.left = self.left.next

        #m,n同时进行改变
        self.recurseAndReverse(right, m - 1, n - 1)
        #利用回溯的过程中，数据回代的特点
        #当两者交叉时，说明转置完成
        if self.left == right or right.next == self.left:
            self.stop = True

        #如果转置未完成
        if not self.stop:
            self.left.val, right.val = right.val, self.left.val  # 两个数的调换
            self.left = self.left.next

#写法2
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        left = head
        right = head
        stop = False

        def recurseAndReverse(right, m, n):
            #nolocal 的使用场景就比较单一，它是使用在闭包中的，使变量使用外层的同名变量
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # keep moving left pointer to the right until we reach the proper node
            # proper node is from where the reversal is to start
            if m > 1:
                left = left.next

            # Recurse with m and n reduced
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we stop
            # i.e. don't swap data any further. We are done reversing at this pointer
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers

            if not stop:
                left.val, right.val = right.val, left.val #两个数的调换
                #不能是
                # left.val = right.val
                # right.val = left.val
                #只能是
                # x = right.val
                # right.val = left.val
                #left.val = x


                # Move left one step to the right
                # The right pinter moves one step back via backtracking

                left = left.next

        recurseAndReverse(right, m, n)
        return head

        
head = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
head.next = b
b.next = c
c.next = d
d.next = e

rl = Solution()
print(rl.reverseBetween(head,1,4).val)