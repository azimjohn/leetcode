package main

func main() {

}

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	odd := &ListNode{Val: head.Val}
	even := &ListNode{Val: head.Next.Val}
	oddHead := odd
	evenHead := even

	head = head.Next.Next

	i := 0
	for head != nil {
		if i%2 == 0 {
			odd.Next = &ListNode{Val: head.Val}
			odd = odd.Next
		} else {
			even.Next = &ListNode{Val: head.Val}
			even = even.Next
		}

		head = head.Next
		i++
	}

	odd.Next = evenHead
	return oddHead
}
