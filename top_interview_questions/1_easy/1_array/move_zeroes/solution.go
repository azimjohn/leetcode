package main

import "fmt"

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeroes(nums)
	fmt.Println(nums) // expected []int{1, 3, 12, 0, 0}
}

func moveZeroes(nums []int) {
	zeroIndex := -1

	for i, num := range nums {
		if num == 0 && zeroIndex == -1 {
			zeroIndex = i
		}
		if num != 0 && zeroIndex != -1 {
			nums[zeroIndex] = num
			nums[i] = 0
			zeroIndex++
		}
	}
}
