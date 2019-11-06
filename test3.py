class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.left = None
        self.stop = None

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        self.left = head
        self.stop = False

        right = head
        self.recurseAndReverse(right, m, n)
        return head

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
print(rl.reverseBetween(head,2,4).val)