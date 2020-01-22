package main

import "fmt"

func main() {
	fmt.Println(hammingWeight(1)) // expected 1
	fmt.Println(hammingWeight(4)) // expected 1
	fmt.Println(hammingWeight(5)) // expected 2
}

func hammingWeight(n uint32) int {
	x := int(n)
	numOnes := 0

	for x != 0 {
		numOnes += x & 1
		x = x >> 1
	}

	return numOnes
}
