package main

import "fmt"

func main() {
	a := &ListNode{
		Val: 2,
		Next: &ListNode{
			Val:  4,
			Next: &ListNode{Val: 3},
		},
	}
	b := &ListNode{
		Val: 5,
		Next: &ListNode{
			Val:  6,
			Next: &ListNode{Val: 4},
		},
	}

	sum := addTwoNumbers(a, b)
	for sum != nil {
		fmt.Print(sum.Val, " ")
		sum = sum.Next
	}
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	sum := l1.Val + l2.Val
	carry := int(sum / 10)
	result := &ListNode{Val: sum % 10}
	resultHead := result

	l1 = l1.Next
	l2 = l2.Next

	for l1 != nil || l2 != nil {
		sum = carry

		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		carry = int(sum / 10)
		result.Next = &ListNode{Val: sum % 10}
		result = result.Next
	}

	if carry != 0 {
		result.Next = &ListNode{Val: carry}
	}

	return resultHead
}
