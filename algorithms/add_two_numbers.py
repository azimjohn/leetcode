# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_ = l1.val + l2.val
        carry = sum_ // 10
        result = ListNode(sum_ % 10)
        result_head = result

        l1 = l1.next
        l2 = l2.next

        while l1 or l2:
            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum_ // 10
            result.next = ListNode(sum_ % 10)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

            result = result.next

        if carry:
            result.next = ListNode(carry)

        return result_head
