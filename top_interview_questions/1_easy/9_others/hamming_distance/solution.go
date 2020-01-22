package main

import "fmt"

func main() {
	fmt.Println(hammingDistance(3, 8)) // expected 3
}

func hammingDistance(x, y int) int {
	xor := x ^ y
	difference := 0

	for xor != 0 {
		difference += xor & 1
		xor = xor >> 1
	}

	return difference
}
