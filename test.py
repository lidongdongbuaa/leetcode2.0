
s='ddddd'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

numb = 1234

pre = new_list = ListNode(0)
for elem in reversed(str(numb)):
    new = ListNode(int(elem))
    pre.next = new
    pre = pre.next

print(new_list.next.val)