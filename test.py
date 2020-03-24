class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

d = a
a.val = 4

print(d.val)