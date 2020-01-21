package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	length := getLength(head)

	if n == 1 && length == 1 {
		return nil
	}

	return removeNthElement(head, length-n)
}

func removeNthElement(head *ListNode, n int) *ListNode {
	node := head

	for i := 0; i < n-1; i++ {
		node = node.Next
	}

	if node.Next != nil {
		if n == 0 {
			node.Val = node.Next.Val
		}
		node.Next = node.Next.Next
	}

	return head
}

func getLength(head *ListNode) int {
	i := 0

	for head != nil {
		head = head.Next
		i++
	}

	return i
}
