package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(increasingTriplet([]int{1, 2, 3, 4, 5})) // true
	fmt.Println(increasingTriplet([]int{5, 4, 3, 2, 1})) // false
}

func increasingTriplet(nums []int) bool {
	if len(nums) == 0 {
		return false
	}

	min := nums[0]
	middle := math.MinInt32

	for _, num := range nums[1:] {
		if min > num {
			min = num
		}

		if middle == math.MinInt32 {
			if num > min {
				middle = num
			}
			continue
		}

		if middle > num && num > min {
			middle = num
		}

		if num > middle && middle > min {
			return true
		}
	}

	return false
}
