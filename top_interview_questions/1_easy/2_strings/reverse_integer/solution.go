package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(reverse(120)) // expected 21
	fmt.Println(reverse(712)) // expected 217
}

func reverse(x int) int {
	var digit int
	y := 0

	if x < math.MinInt32 || x > math.MaxInt32 {
		return 0
	}

	for x != 0 {
		digit = x % 10
		x = x / 10
		y *= 10
		y += digit
	}

	return y
}
