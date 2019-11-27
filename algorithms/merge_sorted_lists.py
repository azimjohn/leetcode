# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        merged_list = None
        merged_list_head = None

        while any(lists):
            smallest_index = self.get_smallest_index(lists)
            if not merged_list:
                merged_list = lists[smallest_index]
                merged_list_head = merged_list
            else:
                merged_list.next = lists[smallest_index]
                merged_list = merged_list.next

            lists[smallest_index] = lists[smallest_index].next

        return merged_list_head

    @staticmethod
    def get_smallest_index(lists):
        smallest = float('inf')
        smallest_index = 0

        for i, l in enumerate(lists):
            if l and l.val < smallest:
                smallest = l.val
                smallest_index = i

        return smallest_index

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


if __name__ == "__main__":
    s = Solution()

    l1 = s.l2ll([1, 4, 5])
    l2 = s.l2ll([1, 3, 4])
    l3 = s.l2ll([2, 6])

    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    merged_list = Solution().mergeKLists([l1, l2, l3])
    print(s.ll2l(merged_list))
    print("PASS" if expected == s.ll2l(merged_list) else "FAIL")
