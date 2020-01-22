# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.getLength(head)

        if n == 1 and length == 1:
            return None

        return self.removeNthElement(head, length - n)

    def removeNthElement(self, head: ListNode, n: int) -> ListNode:
        node = head
        for _ in range(n - 1):
            node = node.next

        if node.next:
            if n == 0:
                node.val = node.next.val
            node.next = node.next.next

        return head

    def getLength(self, head: ListNode) -> int:
        if not head:
            return 0

        return self.getLength(head.next) + 1