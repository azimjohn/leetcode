package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(majorityElement([]int{1, 2, 2, 2, 3, 4}))
}

func majorityElement(nums []int) int {
	l := len(nums)
	sort.Ints(nums)

	return nums[l/2]
}
