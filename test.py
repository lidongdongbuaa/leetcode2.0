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
        while l1 and l2:
            if l1.val + l2.val + i == 10:
                curr.next = ListNode(0)
                i = 1
            else:
                curr.next = ListNode(l1.val + l2.val + i)
                i = 0
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        if i == 0:
            if l1 is None:
                curr.next = l2
            elif l2 is None:
                curr.next = l1
        elif i == 1:
            if l1 is None and l2 is not None:
                curr.next = self.addOne(l2)
            elif l2 is None and l1 is not None:
                curr.next = self.addOne(l1)
            elif l1 is None and l2 is None:
                curr.next = ListNode(1)

        return new_head.next

b = ListNode(5)
a = ListNode(5)
x = Solution()
x.addTwoNumbers(a,b)
