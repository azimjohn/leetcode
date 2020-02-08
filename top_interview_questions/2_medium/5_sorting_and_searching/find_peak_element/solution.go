package main

func main() {

}

func findPeakElement(nums []int) int {
	left := 0
	right := len(nums)

	for left < right {
		mid := (left + right) / 2
		if nums[mid] > nums[mid+1] {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}
