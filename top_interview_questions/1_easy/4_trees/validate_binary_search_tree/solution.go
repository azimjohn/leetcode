package main

import (
	"fmt"
	"math"
)

func main() {
	tree := &TreeNode{
		Val: 2,
		Left: &TreeNode{
			Val: 1,
		},
		Right: &TreeNode{
			Val: 3,
		},
	}
	fmt.Print(isValidBST(tree)) // expected true
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	return helper(root, math.MinInt16, math.MaxInt16)
}

func helper(root *TreeNode, min, max int) bool {
	if root == nil {
		return true
	}

	if root.Val < min || root.Val > max {
		return false
	}

	return helper(root.Left, min, root.Val) && helper(root.Right, root.Val, max)
}
