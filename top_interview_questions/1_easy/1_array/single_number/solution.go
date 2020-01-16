package main

import "fmt"

func main() {
	fmt.Println(singleNumber([]int{1, 2, 2, 3}))    // expected 2
	fmt.Println(singleNumber([]int{2, 3, 4, 5, 5})) // expected 5
}

func singleNumber(nums []int) int {
	xorSum := 0

	for _, num := range nums {
		xorSum ^= num
	}

	return xorSum
}
