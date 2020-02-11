# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        l = head
        prev = None

        while l:
            if prev and l.val == val:
                prev.next = l.next
                l = l.next
                continue

            prev = l
            l = l.next

        if head and head.val == val:
            return head.next

        return head
