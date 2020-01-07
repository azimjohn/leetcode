# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headB:
            headB.is_b = True
            headB = headB.next

        while headA:
            if hasattr(headA, "is_b"):
                return headA

            headA = headA.next
