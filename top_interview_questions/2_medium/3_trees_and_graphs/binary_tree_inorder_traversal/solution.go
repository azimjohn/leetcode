package main

func main() {

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	var result []int
	var s stack
	current := root

	for len(s) != 0 || current != nil {
		for current != nil {
			s = s.Push(current)
			current = current.Left
		}

		s, current = s.Pop()
		result = append(result, current.Val)
		current = current.Right
	}

	return result
}

type stack []*TreeNode

func (s stack) Push(v *TreeNode) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, *TreeNode) {
	l := len(s)
	return s[:l-1], s[l-1]
}
