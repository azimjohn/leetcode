package main

import "fmt"

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1}))    // expected 4
	fmt.Println(rob([]int{2, 7, 9, 3, 1})) // expected 12
}

func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	if len(nums) == 1 {
		return nums[0]
	}

	dp := make([]int, len(nums))
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])

	for i := 2; i < len(dp); i++ {
		dp[i] = max(dp[i-1], dp[i-2]+nums[i])
	}

	return dp[len(dp)-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
