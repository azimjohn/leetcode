package main

import "fmt"

func main() {
	fmt.Println(plusOne([]int{1, 9, 9, 9})) // expected []int{2, 0, 0, 0}
}

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] == 9 {
			digits[i] = 0
		} else {
			digits[i] = digits[i] + 1
			break
		}
	}

	if digits[0] == 0 {
		digits = append([]int{1}, digits...)
	}

	return digits
}
