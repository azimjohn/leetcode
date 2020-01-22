package main

import (
	"fmt"
)

func main() {
	fmt.Println(missingNumber([]int{0, 1, 2, 3, 5})) // expected 4
	fmt.Println(missingNumber([]int{0, 1, 2, 3}))    // expected 4
}

func missingNumber(nums []int) int {
	length := len(nums)
	result := (length + 1) * length / 2

	for i := 0; i < length; i++ {
		result -= nums[i]
	}

	return result
}
