class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None

class Solution:
    def pop(self, head):
        pop_node = head
        head = head.next
        pop_node.next = None
        return pop_node.val

'''
test case
'''
A1 = Node(3)
A2 = Node(4)
A3 = Node(1)

A1.next = A2
A2.next = A3


X = Solution()
print(X.pop(A1))