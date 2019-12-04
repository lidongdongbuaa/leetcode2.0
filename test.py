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









