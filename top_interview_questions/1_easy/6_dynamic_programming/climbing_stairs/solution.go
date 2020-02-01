package main

import "fmt"

func main() {
	fmt.Println(climbStairs(2))
	fmt.Println(climbStairs(3))
	fmt.Println(climbStairs(4))
	fmt.Println(climbStairs(5))
}

func climbStairs(n int) int {
	return fib(n)
}

func fib(n int) int {
	a, b := 0, 1

	for a < n {
		a, b = b, a+b
	}

	return b
}
