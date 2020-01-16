package main

import "fmt"

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1})) // expected true
	fmt.Println(containsDuplicate([]int{1, 2, 3, 4})) // expected false
}

func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)

	for _, num := range nums {
		if seen[num] {
			return true
		}
		seen[num] = true
	}

	return false
}
