# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         self.visited = False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if hasattr(head, "visited"):
                return True
            
            head.visited = True
            head = head.next
        
        return False
