package main

import "fmt"

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	rotate(nums, 3)
	fmt.Println(nums) // expected [5,6,7,1,2,3,4]
}

func rotate(nums []int, k int) {
	length := len(nums)
	k = k % length
	rotated := nums[length-k:]

	rotated = append(rotated, nums[:length-k]...)

	for i := 0; i < length; i++ {
		nums[i] = rotated[i]
	}
}
