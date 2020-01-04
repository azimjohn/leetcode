# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# TODO: improve
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array_list = []

        while head:
            array_list.append(head.val)
            head = head.next

        return array_list == array_list[::-1]
