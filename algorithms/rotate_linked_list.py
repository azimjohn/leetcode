# https://leetcode.com/problems/rotate-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        
        l = self.ll2l(head)
        l = self.rotateList(l, k)
        ll = self.l2ll(l)

        return ll
    
    @staticmethod
    def ll2l(ll):
        l = []
        
        while ll:
            l.append(ll.val)
            ll = ll.next
            
        return l

    @staticmethod
    def l2ll(l):
        head = ListNode(l[0])
        current = head
        
        for li in l[1:]:
            current.next = ListNode(li)
            current = current.next
    
        return head
    
    
    @staticmethod
    def rotateList(l, k):
        k = k % len(l)
        l = l[len(l) - k:] + l[:len(l) - k]

        return l
