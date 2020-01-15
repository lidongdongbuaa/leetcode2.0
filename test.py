class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class mySolution:
    def sortLinklist(self, head):
        if not head:  # corner case
            return None
        if not head.next:
            return head

        length = self.findL(head)  # calculate length
        interval = 1
        dummy = ListNode(0)
        dummy.next = head


        while interval < length:  # do bottom-up merge
            fake_tail = dummy  # fake_tail is tail of last part, 初始化
            head  = dummy.next
            while head:
                nextH = self.cut(head, interval)
                leftH = self.cut(nextH, interval)
                mergeHead, mergeTail = self.merge(head, nextH)
                fake_tail.next = mergeHead  # connect the merged part to original linklist
                mergeTail.next = leftH
                fake_tail = mergeTail  # renew the tail which is before the merge sort part
                head = leftH # renew the head
            interval = 2 * interval

        return dummy.next

    def findL(self, head):  # calculate lenght
        if not head: # corner case
            return 0

        numb = 0
        while head:  # accumlate length
            head = head.next
            numb += 1
        return numb

    def cut(self, head, interval): # from head to cut interval nodes, return next part head
        if not head: # corner case
            return None

        for _ in range(interval):
            if not head:  # corner case: interval > length of linklist
                break
            tail = head
            head = head.next
        tail.next = None
        return head

    def merge(self, head1, head2): # merge sort two sorted linklist. return this part head and tail
        if not head1:
            cur = head2
            while cur.next:
                cur = cur.next
            return head2, cur
        if not head2:
            cur = head1
            while cur.next:
                cur = cur.next
            return head1, cur

        dummy = cur = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next

        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        while cur.next:
            cur = cur.next
        return dummy.next, cur


A1 = ListNode(5)
A2 = ListNode(4)
A3 = ListNode(3)
A4 = ListNode(2)
A5 = ListNode(1)
A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5

x = mySolution()
print(x.sortLinklist(A1).val)



