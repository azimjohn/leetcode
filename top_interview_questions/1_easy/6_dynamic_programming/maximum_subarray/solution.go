package main

func main() {

}

func maxSubArray(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	maxSum, currSum := nums[0], nums[0]

	for _, num := range nums[1:] {
		currSum = max(currSum+num, num)

		if currSum > maxSum {
			maxSum = currSum
		}
	}

	return maxSum
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
