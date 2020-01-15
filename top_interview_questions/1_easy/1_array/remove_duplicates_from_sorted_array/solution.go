package main

import "fmt"

func main() {
	nums := []int{1, 1, 2, 3, 3, 4, 4}
	fmt.Println(removeDuplicates(nums))
	fmt.Println(nums)
}

func removeDuplicates(nums []int) int {
	prev := 0
	n := 0

	for i, num := range nums {
		if i == 0 || num != prev {
			nums[n] = num
			n += 1
		}
		prev = num
	}

	return n
}
