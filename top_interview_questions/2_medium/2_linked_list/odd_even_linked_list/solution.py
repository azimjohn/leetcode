# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even = ListNode(head.val)
        odd = ListNode(head.next.val)
        even_head = even
        odd_head = odd
        head = head.next.next

        i = 0
        while head:
            if i % 2 == 0:
                even.next = ListNode(head.val)
                even = even.next
            else:
                odd.next = ListNode(head.val)
                odd = odd.next

            head = head.next
            i += 1

        even.next = odd_head
        return even_head
