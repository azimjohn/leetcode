package main

import "fmt"

func main() {
	l1 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 3,
			},
		},
	}
	l2 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 1,
			},
		},
	}
	fmt.Println(isPalindrome(l1)) // expected false
	fmt.Println(isPalindrome(l2)) // expected true
}

type stack []int

func (s stack) Push(v int) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, int) {
	l := len(s)
	return s[:l-1], s[l-1]
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	s := stack{}
	curr := head
	var val int

	for curr != nil {
		s = s.Push(curr.Val)
		curr = curr.Next
	}

	curr = head
	for curr != nil {
		s, val = s.Pop()
		if val != curr.Val {
			return false
		}
		curr = curr.Next
	}

	return true
}
