class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:  # edge case, head is None
            head = Node(insertVal)
            head.next = head
            return head

        prev, curr = head, head.next
        toInsert = False

        while True:  # iterative node, four case of node
            if prev.val <= insertVal <= curr.val:  # case 1/4
                toInsert = True
            elif prev.val > curr.val:
                if prev.val <= insertVal or insertVal <= curr.val:  # case 2/3
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)  # mission accomplished
                return head

            prev, curr = curr, curr.next
            if prev == head:
                break

        prev.next = Node(insertVal, curr)  # case 5, did not insert the node in the loop
        return head

'''
test case
'''
A1 = Node(3)
A2 = Node(4)
A3 = Node(1)

A1.next = A2
A2.next = A3
A3.next = A1

X = Solution()
print(X.insert(A1, 2))