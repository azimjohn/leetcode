package main

import "fmt"

func main() {
	ll := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val:  2,
			Next: nil,
		},
	}
	fmt.Println(hasCycle(ll)) // expected false
	ll.Next.Next = ll
	fmt.Println(hasCycle(ll)) // expected true
}

type ListNode struct {
	Val  int
	Next *ListNode
}

// uses extra O(n) space
func _hasCycle(head *ListNode) bool {
	visited := make(map[*ListNode]bool)
	var exists bool

	for head != nil {
		_, exists = visited[head]
		if exists {
			return true
		}
		visited[head] = true
		head = head.Next
	}

	return false
}

// with O(1) space + 2 times faster
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	slow := head
	fast := head.Next

	for slow != nil && fast != nil && fast.Next != nil {
		if slow == fast {
			return true
		}
		slow = slow.Next
		fast = fast.Next.Next
	}

	return false
}
