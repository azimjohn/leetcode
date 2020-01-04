# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# TODO: improve
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next

        list_vals = list_vals[::-1]
        reversed_list = ListNode(list_vals[0])
        reversed_list_head = reversed_list

        for val in list_vals[1:]:
            reversed_list.next = ListNode(val)
            reversed_list = reversed_list.next

        return reversed_list_head
