class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertNode(self, head, insertVal):
        next_node = head.next
        new_node = Node(insertVal)
        head.next = new_node
        new_node.next = next_node

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:  # edge case, head is None
            head = Node(insertVal)
            head.next = head
            return head

        ref = head  # backup head
        head = head.next
        repeat = 0  # 0 -> linklist is not full of repeated node
        while ref is not head:  # judge whether linklist is full of repeated node
            if ref.val != head.val:
                break
            head = head.next
        else:
            repeat = 1

        if repeat == 1:  # linklist is full of repeated node
            self.insertNode(head, insertVal)
            return head
        else:  # linklist is not full of repeated node
            ref = head
            while head:  # iterative node, four case of node
                if insertVal == head.val:
                    self.insertNode(head, insertVal)
                    return ref
                elif insertVal > head.val > head.next.val:
                    self.insertNode(head, insertVal)
                    return ref
                elif insertVal < head.next.val < head.val:
                    self.insertNode(head, insertVal)
                    return ref
                elif head.val < insertVal < head.next.val:
                    self.insertNode(head, insertVal)
                    return ref
                head = head.next


'''
test case
'''
A1 = Node(3)
A2 = Node(3)
A3 = Node(3)

A1.next = A2
A2.next = A3
A3.next = A1

X = Solution()
print(X.insert(A1, 0))