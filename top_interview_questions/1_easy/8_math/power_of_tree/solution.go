package main

import "fmt"

func main() {
	fmt.Println(isPowerOfThree(27))  // expected true
	fmt.Println(isPowerOfThree(818)) // expected false
}

func isPowerOfThree(n int) bool {
	if n == 1 {
		return true
	}

	if n < 1 || n%3 != 0 {
		return false
	}

	return isPowerOfThree(n / 3)
}
