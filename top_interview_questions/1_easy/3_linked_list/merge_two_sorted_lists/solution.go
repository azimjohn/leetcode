package main

import "fmt"

func main() {
	l1 := &ListNode{
		Val: 2,
		Next: &ListNode{
			Val: 3,
		},
	}
	l2 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 4,
		},
	}
	merged := mergeTwoLists(l1, l2)
	for merged != nil {
		fmt.Print(merged.Val, " ")
		merged = merged.Next
	}
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	mergedHead := &ListNode{Val: 0}
	current := mergedHead

	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			current.Next = &ListNode{Val: l1.Val}
			l1 = l1.Next
		} else {
			current.Next = &ListNode{Val: l2.Val}
			l2 = l2.Next
		}
		current = current.Next
	}

	if l1 != nil {
		current.Next = l1
	}
	if l2 != nil {
		current.Next = l2
	}

	return mergedHead.Next
}
