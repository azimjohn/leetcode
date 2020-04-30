# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        current = head
        prev = current
        current = current.next
        
        while current:
            if current.val == prev.val:
                if current.next:
                    current.val = current.next.val
                    current.next = current.next.next
                else:
                    prev.next = None

            prev = current
            current = current.next
        
        return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)

l = Solution().deleteDuplicates(head)
while l:
    print(l.val)
    l = l.next
