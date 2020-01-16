package main

import (
	"fmt"
)

func main() {
	fmt.Println(intersect([]int{1, 2, 2, 1}, []int{2, 2})) // expected []int{2, 2}
}

func intersect(nums1 []int, nums2 []int) []int {
	var result []int
	counter1 := counter(nums1)
	counter2 := counter(nums2)

	for num, count := range counter1 {
		minCount := min(count, counter2[num])
		for i := 0; i < minCount; i++ {
			result = append(result, num)
		}
	}

	return result
}

func counter(nums []int) map[int]int {
	c := make(map[int]int)

	for _, num := range nums {
		c[num]++
	}

	return c
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
