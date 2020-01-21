package main

import "fmt"

func main() {
	ll := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 3,
			},
		},
	}
	ll = reverseList(ll)
	for ll != nil {
		fmt.Print(ll.Val, " ")
		ll = ll.Next
	} // expected 3 2 1
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	var next *ListNode

	for head != nil {
		next = head.Next
		head.Next = prev
		prev = head
		head = next
	}

	return prev
}
