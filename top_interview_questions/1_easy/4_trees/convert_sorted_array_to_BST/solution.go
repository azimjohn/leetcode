package main

import "fmt"

func main() {
	tree := sortedArrayToBST([]int{1, 2, 3})
	fmt.Println(tree.Val)       // expected 2
	fmt.Println(tree.Left.Val)  // expected 1
	fmt.Println(tree.Right.Val) // expected 3
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}

	middle := len(nums) / 2
	left := sortedArrayToBST(nums[:middle])
	right := sortedArrayToBST(nums[middle+1:])

	root := &TreeNode{
		nums[middle],
		left,
		right,
	}

	return root
}
