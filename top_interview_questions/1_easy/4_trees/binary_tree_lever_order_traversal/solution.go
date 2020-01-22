package main

import "fmt"

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
	fmt.Println(levelOrder(tree))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	depth := maxDepth(root)
	levels := make([][]int, depth)
	fmt.Println(levels)
	helper(root, 0, levels)

	return levels
}

func helper(root *TreeNode, level int, levels [][]int) {
	if root == nil || level == len(levels) {
		return
	}

	levels[level] = append(levels[level], root.Val)
	helper(root.Left, level+1, levels)
	helper(root.Right, level+1, levels)
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftMaxDepth := maxDepth(root.Left)
	rightMaxDepth := maxDepth(root.Right)

	if leftMaxDepth > rightMaxDepth {
		return leftMaxDepth + 1
	}

	return rightMaxDepth + 1
}
