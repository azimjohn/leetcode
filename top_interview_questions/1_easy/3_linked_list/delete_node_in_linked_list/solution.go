package main

import "fmt"

func main() {
	ll := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val:  3,
				Next: nil,
			},
		},
	}
	deleteNode(ll)           // deletes 1
	fmt.Println(ll.Val)      // expected 2
	fmt.Println(ll.Next.Val) // expected 3
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}
