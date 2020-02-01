package main

import "math/rand"

type Solution struct {
	nums     []int
	original []int
}

func Constructor(nums []int) Solution {
	original := make([]int, len(nums))
	copy(original, nums)

	return Solution{
		nums:     nums,
		original: original,
	}
}

/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
	this.nums = this.original

	return this.original
}

/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
	var randIndex int
	length := len(this.nums)

	for i := 0; i < length; i++ {
		randIndex = rand.Intn(length)
		this.nums[i], this.nums[randIndex] = this.nums[randIndex], this.nums[i]
	}

	return this.nums
}
