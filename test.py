class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:  # sort linklist
        if not head:  # edge case
            return None
        if not head.next:  # edge case
            return head

        length = 10  # calcu length of linklist

        dummy = former_tail = ListNode(None)
        dummy.next = head
        interval = 1
        # 要求： 保持整体的head可以输出，保证段与段的连接
        while interval < length:  # bottom - up merge sort
            head1 = dummy.next
            n = 1
            while head1:
                head2 = self.split(head1, interval)  # cut group1, return next adjacent group head
                next_head1 = self.split(head2,
                                        interval)  # cut group 1's adjacent group 2, return next adjacent group head
                merge_start, merge_end = self.merge(head1, head2)  # merge group1 and group2

                if n == 1:
                    dummy.next = merge_start
                    former_tail = merge_end
                else:
                    former_tail.next = merge_start
                    former_tail = merge_end
                head1 = next_head1
                n += 1
            interval = 2 * interval

        return dummy.next

    def find_len(self, head):  # calculate the lenght of linklist
        if not head:  # edge case
            return 0
        if not head.next:  # edge case
            return 1

        length = 0
        curr = head
        while curr:  # accumulate length
            length += 1
            curr = curr.next
        return length

    def split(self, head, interval):  # cut the group from the linklist, return next adjacent group head
        if not head:
            return head

        for _ in range(interval - 1):
            if not head.next:  # not enough node for travel
                break
            head = head.next

        tail = head.next
        head.next = None
        return tail

    def merge(self, head1, head2):  # merge group1 and group2, return merged head and tail
        dummy = tail = ListNode(0)
        while head1 and head2:  # merge two group
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        while tail.next:  # let tail points to the end of merged linked list
            tail = tail.next
        return dummy.next, tail



def makeLinklist(arr):
    dummy =head = ListNode(None)
    for elem in arr:
        newNode = ListNode(elem)
        dummy.next = newNode
        dummy = dummy.next
    return head.next

A1 = makeLinklist([4, 3, 2, 1])
X = Solution()
print(X.sortList(A1).val)